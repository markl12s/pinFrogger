"""
------------------------------------------------------------------------------------------------------------------
pinFrogger: frogger but the goal is to enter the computers pin, numbers 0-9 are the spots on top of the screen
post on /r/badUIbattles when done

last update: 4/30/2022

current task: debugging

next task: create drawing background, use turtles to draw and fill in the different sections
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
window.bgcolor('black')

playerDead = False

isTesting = True


"""
------------------------------------------------------------------------------------------------------------------
player
------------------------------------------------------------------------------------------------------------------
"""

class Player:
    playerSize = 1.5
    playerSpeed = 30 * playerSize

    # constructor
    def __init__(self, name='player', size=playerSize):
        self.turtle = turtle.Turtle()
        self.turtle.shape('square')
        self.turtle.color('light green')
        self.turtle.shapesize(size, size)
        self.turtle.penup()

    # movement
    def move_left(self, speed=playerSpeed):
        movement('left', speed, player.turtle)

    def move_right(self, speed=playerSpeed):
        movement('right', speed, player.turtle)

    def move_up(self, speed=playerSpeed):
        movement('up', speed, player.turtle)

    def move_down(self, speed=playerSpeed):

        movement('down', speed, player.turtle)


"""
------------------------------------------------------------------------------------------------------------------
misc functions
------------------------------------------------------------------------------------------------------------------
"""

def movement(direction, speed, actor):
    speed = speed
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
testing functions
------------------------------------------------------------------------------------------------------------------
"""

def test_player_movement():
    sleepTime = 0.25
    startX, startY = player.turtle.position()

    player.move_left()
    time.sleep(sleepTime)
    player.move_right()
    time.sleep(sleepTime)

    if startX == player.turtle.xcor():
        print('horizontal test passed')

    player.move_up()
    time.sleep(sleepTime)
    player.move_down()

    if startY == player.turtle.ycor():
        print('vertical test passed')


"""
------------------------------------------------------------------------------------------------------------------
set up game
------------------------------------------------------------------------------------------------------------------
"""

player = Player('frog')


"""
------------------------------------------------------------------------------------------------------------------
execution
------------------------------------------------------------------------------------------------------------------
"""

if isTesting:
    test_player_movement()

while not playerDead:
    turtle.update()

