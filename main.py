"""
pinFrogger: frogger but the goal is to enter the computers pin, post on /r/badUIbattles when done

last update: 4/30/2022

current task: make the frog work on a grid
"""

import turtle

window = turtle.Screen()

player = turtle.Turtle()
player.shape('square')
player.penup
playerSpeed = 30

playerDead = False


"""
------------------------------------------------------------------------------------------------------------------
functions
------------------------------------------------------------------------------------------------------------------
"""

def movement(direction, speed, actor):
    x, y = player.position()

    moveDirection = {
        'left': [-abs(speed), 0],
        'right': [speed, 0],
        'up': [0, speed],
        'down': [0, -abs(playerSpeed)]
    }

    move = moveDirection.get(direction)
    actor.goto((x + int(move[0])), (y + int(move[1])))


"""
------------------------------------------------------------------------------------------------------------------
execution
------------------------------------------------------------------------------------------------------------------
"""

while not playerDead:
    movement('right', playerSpeed, player)
