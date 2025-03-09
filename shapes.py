import pgzrun
from random import randint

WIDTH = 300
HEIGHT = 300

def draw():
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    width = WIDTH-100
    height = HEIGHT - 200
    screen.fill("black")
    screen.draw.circle((150,150),100,"red")
    r1=Rect((0,0),(width,height))
    r1.center=150,150
    screen.draw.rect(r1,(r,g,b))
    screen.draw.line((150,150),(210,150),('green'))
    screen.draw.line((150,150),(180,100),('green'))
    screen.draw.line((180,100),(210,150),('green'))
pgzrun.go()