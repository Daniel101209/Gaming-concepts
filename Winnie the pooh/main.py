import pgzrun
from random import randint

WIDTH=600
HEIGHT=500

winnie=Actor("winnie")
winnie.pos=100,100

honeyjar=Actor("jar")
honeyjar.pos=500,400

score=0
game_over=False

def draw():
    screen.fill("yellow")
    winnie.draw()
    honeyjar.draw()
    screen.draw.text("Score= "+str(score),color="cyan",topleft=(10,10))

    if game_over:
        screen.fill("black")
        screen.draw.text("Time's up! Your final score is "+str(score),midtop=(WIDTH/2,10),color="cyan")

def time_up():
    global game_over
    game_over=True

def place_honey():
    honeyjar.x=randint(50,WIDTH-50)
    honeyjar.y=randint(0,HEIGHT-30)

def update():
    global score

    if keyboard.left:
        winnie.x = winnie.x -2
    if keyboard.right:
        winnie.x = winnie.x +2
    if keyboard.up:
        winnie.y = winnie.y -2
    if keyboard.down:
        winnie.y = winnie.y +2

    collect=winnie.colliderect(honeyjar)

    if collect:
        score=score+10
        place_honey()

clock.schedule(time_up,60.0)

pgzrun.go()