"""
------------------------------------------------------------------------------------------------------------------
pinFrogger: frogger but the goal is to enter the computers pin, numbers 0-9 are the spots on top of the screen
post on /r/badUIbattles when done
last update: 6/23/2022
current task: refactoring

next task: fix the button queue feature

know bugs:

note: in the future, make sure the window fully initializes before calling any constructors
------------------------------------------------------------------------------------------------------------------
"""

import turtle
import time


"""
------------------------------------------------------------------------------------------------------------------
setup
------------------------------------------------------------------------------------------------------------------
"""

window = turtle.Screen()
window.setworldcoordinates(0, 0, 100, 100)
window.bgcolor('black')

playerLives = 3


"""
------------------------------------------------------------------------------------------------------------------
player
------------------------------------------------------------------------------------------------------------------
"""

class Player:
    rowSize = 100 / 12
    playerSize = rowSize - 6
    playerSpeed = rowSize
    keyPressed = 0
    buttonQueue = []

    # constructor
    def __init__(self, name='player', size=playerSize):
        self.turtle = turtle.Turtle()
        self.turtle.shape('square')
        self.turtle.color('light green')
        self.turtle.shapesize(size, size)
        self.turtle.penup()

    # controls
    def playerControls(self):
        turtle.listen()

        window.onkeypress(player.move_up, 'Up')
        window.onkeypress(player.move_down, 'Down')
        window.onkeypress(player.move_left, 'Left')
        window.onkeypress(player.move_right, 'Right')

        window.onkeyrelease(player.key_flop, 'Up')
        window.onkeyrelease(player.key_flop, 'Down')
        window.onkeyrelease(player.key_flop, 'Left')
        window.onkeyrelease(player.key_flop, 'Right')

    def key_flop(self):
        player.keyPressed -= 1
        player.keyPressed = abs(player.keyPressed)

    # movement
    def move_left(self, speed=playerSpeed):
        if player.keyPressed == 0:
            movement('left', speed, player.turtle)
            player.key_flop()
        else:
            player.buttonQueue.append('left')

    def move_right(self, speed=playerSpeed):
        if player.keyPressed == 0:
            movement('right', speed, player.turtle)
            player.key_flop()
        else:
            player.buttonQueue.append('right')

    def move_up(self, speed=playerSpeed):
        if player.keyPressed == 0:
            movement('up', speed, player.turtle)
            player.key_flop()
        else:
            player.buttonQueue.append('up')

    def move_down(self, speed=playerSpeed):
        if player.keyPressed == 0:
            movement('down', speed, player.turtle)
            player.key_flop()
        else:
            player.buttonQueue.append('down')

    def run_button_queue(self):
        for i in range(len(player.buttonQueue)):
            movement(player.buttonQueue[i], player.playerSpeed, player.turtle)
        player.buttonQueue = []


"""
------------------------------------------------------------------------------------------------------------------
misc functions
------------------------------------------------------------------------------------------------------------------
"""

def movement(direction, speed, actor):
    x, y = actor.position()

    moveDirection = {
        'left': [-abs(speed), 0],
        'right': [speed, 0],
        'up': [0, speed],
        'down': [0, -abs(speed)]
    }

    move = moveDirection.get(direction)
    actor.goto((x + move[0]), (y + move[1]))


"""
------------------------------------------------------------------------------------------------------------------
testing/development tools
------------------------------------------------------------------------------------------------------------------
"""

class Development_tools:
    # tests if player movement moves precisely
    def test_player_movement():
        sleepTime = 0.25
        startX, startY = player.turtle.position()

        player.move_left()
        player.key_flop()
        time.sleep(sleepTime)
        player.move_right()
        player.key_flop()
        time.sleep(sleepTime)

        if startX == player.turtle.xcor():
            print('horizontal test passed')

        player.move_up()
        player.key_flop()
        time.sleep(sleepTime)
        player.move_down()
        player.key_flop()

        if startY == player.turtle.ycor():
            print('vertical test passed')

    # used to show the grid, allowing for checking if movement is moving evenly
    def show_grid():
        gridDrawer = turtle.Turtle()
        gridDrawer.color('white')
        gridDrawer.speed(0)

        interval = 100 / 12
        starts = []
        add = 0

        for i in range(12):
            starts.append(add)
            add += interval

        for x in range(12):
            gridDrawer.penup()
            gridDrawer.goto(starts[x], 0)
            gridDrawer.pendown()
            gridDrawer.goto(starts[x], 100)

        for y in range(12):
            gridDrawer.penup()
            gridDrawer.goto(0, starts[y])
            gridDrawer.pendown()
            gridDrawer.goto(100, starts[y])

        gridDrawer.hideturtle()


"""
------------------------------------------------------------------------------------------------------------------
set up game
------------------------------------------------------------------------------------------------------------------
"""

player = Player('player')
player.turtle.goto(50, 50)

"""
------------------------------------------------------------------------------------------------------------------
execution
------------------------------------------------------------------------------------------------------------------
"""

isTesting = True
if isTesting:
    Development_tools.show_grid()
    # Development_tools.test_player_movement()

while playerLives > 0:
    player.playerControls()
    player.run_button_queue()
    turtle.update()

