import random
import itertools
import pgzrun

WIDTH = 400
HEIGHT = 400

BLOCK_POSITIONS = [(350,50),(350,350),(50,350),(50,50)]

block_positions=itertools.cycle(BLOCK_POSITIONS)

block=Actor('block',center=(50,50))
ship=Actor('ship',center=(200,200))

def draw():
    screen.clear()
    block.draw()
    ship.draw()

def move_block():
    animate(block,'bounce_end',duration=1,pos=next(block_positions))

move_block()
clock.schedule_interval(move_block,2)

pgzrun.go()