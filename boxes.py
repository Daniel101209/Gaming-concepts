import pgzrun
from random import randint

WIDTH =300
HEIGHT=300


def draw():
    screen.fill("black")
    r=255
    g=0
    b=randint(0,255)

    width= WIDTH
    height = HEIGHT - 200

    for i in range(20):
        r1=Rect((0,0),(width,height))
        r1.center=150,150
        screen.draw.rect(r1,(r,g,b))

        r -=10
        g +=10


        width=width-10
        height+=10

pgzrun.go()