"""
------------------------------------------------------------------------------------------------------------------
pinFrogger: frogger but the goal is to enter the computers pin, numbers 0-9 are the spots on top of the screen
post on /r/badUIbattles when done
last update: 6/28/2022
current task: refactor

next task: create logs

known bugs:

note: in the future, make sure the window fully initializes before calling any constructors
this caused a significant bug in development, avoid this bug in the future
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
window.bgcolor('dark blue')


"""
------------------------------------------------------------------------------------------------------------------
drawing objects
------------------------------------------------------------------------------------------------------------------
"""

class Drawing:
    numRows = 15
    numColumns = 10
    lengthScreen = 100
    rowSize, colSize = lengthScreen / numRows, lengthScreen / numColumns

    targetSize = 2
    targetY = 83
    waterBeginY = 37

    grassGreen = [0, 154, 23]

    def draw_board():
        # grass around road
        Drawing.draw_rect([-10, -10], [100, Drawing.rowSize], Drawing.grassGreen)
        Drawing.draw_rect([-10, Drawing.rowSize * 5], [100, Drawing.rowSize * 6], Drawing.grassGreen)

        # road
        Drawing.draw_rect([-10, Drawing.rowSize] , [100, Drawing.rowSize * 5], [0, 0, 0])

        # finishing grass
        Drawing.draw_rect([-10, Drawing.rowSize * 12.5], [100, Drawing.rowSize * 13], Drawing.grassGreen)

        # objective spaces
        add = 0
        for i in range(Drawing.numColumns):
            Drawing.draw_rect([add - Drawing.targetSize, Drawing.rowSize * 12],
                              [add + Drawing.targetSize, Drawing.rowSize * 12.5], Drawing.grassGreen)

            add += Drawing.colSize

    def draw_rect(bottomLeft, topRight, colorRGB):
        # setup pen
        pen = turtle.Turtle()
        turtle.colormode(255)
        pen.color(colorRGB)

        # setup positioning
        pen.penup()
        pen.speed(0)
        pen.goto(bottomLeft)
        pen.pendown()

        # draw rectangle
        pen.begin_fill()
        pen.goto(topRight[0], bottomLeft[1])
        pen.goto(topRight)
        pen.goto(bottomLeft[0], topRight[1])
        pen.goto(bottomLeft)
        pen.end_fill()
        pen.hideturtle()


"""
------------------------------------------------------------------------------------------------------------------
player
------------------------------------------------------------------------------------------------------------------
"""

class Player:
    rowSize = Drawing.rowSize
    playerSize = rowSize - 6
    playerSpeed = rowSize

    playerLives = 3

    keyPressed = 0
    buttonQueue = []
    lastButton = ''

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
    def player_movement(self, direction, speed=playerSpeed):
        if player.keyPressed == 0:
            movement(direction, speed, player.turtle)
            player.lastButton = direction
            player.key_flop()
        elif player.lastButton != direction:
            player.buttonQueue.append(direction)

    def run_button_queue(self):
        for i in range(len(player.buttonQueue)):
            movement(player.buttonQueue[i], player.playerSpeed, player.turtle)
        player.buttonQueue = []

    def move_left(self):
        player.player_movement('left')

    def move_right(self):
        player.player_movement('right')

    def move_up(self):
        player.player_movement('up')

    def move_down(self):
        player.player_movement('down')

    # player behaviors
    def hit_water(self):
        playerX, playerY = player.turtle.position()

        if playerY > Drawing.targetY:
            pass
        else:
            if playerY > Drawing.waterBeginY:
                player.die()

    def die(self):
        player.turtle.hideturtle()
        player.playerLives -= 1
        player.turtle.goto(50, centerSquare)
        player.turtle.showturtle()


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

        interval = Drawing.rowSize
        starts = []
        add = 0

        for i in range(Drawing.numRows):
            starts.append(add)
            add += interval

        for x in range(Drawing.numRows):
            gridDrawer.penup()
            gridDrawer.goto(starts[x], 0)
            gridDrawer.pendown()
            gridDrawer.goto(starts[x], 100)

        for y in range(Drawing.numRows):
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
centerSquare = Drawing.rowSize / 2
player.turtle.goto(50, centerSquare)

Drawing.draw_board()


"""
------------------------------------------------------------------------------------------------------------------
execution
------------------------------------------------------------------------------------------------------------------
"""

isTesting = False
if isTesting:
    i = 0

while player.playerLives > 0:
    player.playerControls()
    player.run_button_queue()
    player.hit_water()
    turtle.update()

    if isTesting:
        i += 1
        if i == 500:
            i = 0

