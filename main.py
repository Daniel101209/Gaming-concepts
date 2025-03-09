import pgzrun
from random import randint

TITLE="Good Shot"

WIDTH = 500
HEIGHT=500

tom=Actor('tom')
tom.pos=50,50
message=""

def draw():
    screen.clear()
    screen.fill("black")
    tom.draw()
    screen.draw.text(message,center=(400,10),fontsize=25)

def place_tom():
    tom.x=randint(50,WIDTH-50)
    tom.y=randint(50,HEIGHT-50)

def on_mouse_down(pos):
    global message
    if tom.collidepoint(pos):
        message="Good shot"
        place_tom()
    else:
       message="Bad shot" 
        
place_tom()
pgzrun.go()