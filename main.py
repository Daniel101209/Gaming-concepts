import pgzrun
from random import randint
from time import time

WIDTH=800
HEIGHT=470

satellites=[]
lines=[]

next_satellite=0
start_time=0
total_time=0
end_time=0
number_of_satellites=8

def create_satellites():
    global start_time
    for i in range(0,number_of_satellites):
        satellite=Actor("sat")
        satellite.pos=randint(40,WIDTH-40),randint(40,HEIGHT-40)
        satellites.append(satellite)
    start_time=time()

def draw():
    screen.blit("bg",(0,0))
    num=1
    for s in satellites:
        screen.draw.text(str(num),(s.pos[0], s.pos[1]+20))
        s.draw()
        num=num+1
create_satellites()
pgzrun.go()