import pgzrun
from random import randint

WIDTH=800
HEIGHT=470

eggs=[]

number_of_eggs=8

def create_eggs():
    for i in range(0,number_of_eggs):
        egg=Actor("egg")
        egg.pos=randint(40,WIDTH-40),randint(40,HEIGHT-40)
        eggs.append(egg)

def draw():
    screen.blit("bgforegg",(0,0))
    num=1
    for s in eggs:
        screen.draw.text(str(num),(s.pos[0], s.pos[1]+20))
        s.draw()
        num=num+1


create_eggs()
pgzrun.go()