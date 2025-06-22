import random
import itertools
import pgzrun

WIDTH = 400
HEIGHT = 400

BALL_POSITIONS = [(350,50),(350,350),(50,350),(50,50)]

block_positions=itertools.cycle(BALL_POSITIONS)

ball=Actor('ball',center=(50,50))
ship=Actor('ship',center=(200,200))

def draw():
    screen.clear()
    ball.draw()
    ship.draw()

def move_ball():
    animate(ball,'bounce_end',duration=1,pos=next(block_positions))

move_ball()
clock.schedule_interval(move_ball,2)

pgzrun.go()