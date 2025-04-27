import pgzrun
from random import randint
from time import time

WIDTH=800
HEIGHT=470

eggs=[]
lines = []
next_egg = 0

start_time=0
total_time=0
end_time=0

number_of_eggs=8

def create_eggs():
    global start_time
    for i in range(0,number_of_eggs):
        egg=Actor("egg")
        egg.pos=randint(40,WIDTH-40),randint(40,HEIGHT-40)
        eggs.append(egg)
    start_time = time()

def draw():
    global total_time
    screen.blit("bgforegg",(0,0))
    num=1
    for s in eggs:
        screen.draw.text(str(num),(s.pos[0], s.pos[1]+20))
        s.draw()
        num=num+1
    for line in lines:
        screen.draw.line(line[0],line[1],"red")
    if next_egg < number_of_eggs:
        total_time=time()-start_time
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)
    else:
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)

def update():
    pass

def on_mouse_down(pos):
    global next_egg, lines
    if next_egg < number_of_eggs:
        if eggs[next_egg].collidepoint(pos):
            if next_egg:
                lines.append((eggs[next_egg-1].pos,eggs[next_egg].pos))
            next_egg=next_egg+1
        else:
            lines=[]
            next_egg


create_eggs()
pgzrun.go()