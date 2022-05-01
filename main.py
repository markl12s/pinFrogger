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

def player_up():
    x, y = player.position()
    player.goto(x, (y + playerSpeed))

def player_down():
    x, y = player.position()
    player.goto(x, (y - playerSpeed))

def player_left():
    x, y = player.position()
    player.goto((x - playerSpeed), y)

def player_right():
    x, y = player.position()
    player.goto((x + playerSpeed), y)


"""
------------------------------------------------------------------------------------------------------------------
execution
------------------------------------------------------------------------------------------------------------------
"""

while not playerDead:
    player_up()

