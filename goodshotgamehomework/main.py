import pgzrun
from random import randint

TITLE = "Good Shot"

WIDTH = 500
HEIGHT = 500

target=Actor('target')
target.pos=(50,50)
message=""

def draw():
    screen.clear
    screen.blit('bgimage',(0,0))
    target.draw()
    screen.draw.text(message,center=(400,10),fontsize=25)

def place_target():
    target.x=randint(50,WIDTH - 50)
    target.y=randint(50,HEIGHT - 50)

def on_mouse_down(pos):
    global message
    if target.collidepoint(pos):
        message = "Good Shot"
        place_target()
    else:
        message = "Bad Shot"

place_target()    
pgzrun.go()