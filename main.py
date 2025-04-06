import pgzrun
from random import randint

WIDTH=600
HEIGHT=500

emmet=Actor("emmet")
emmet.pos=100,100

stud=Actor("stud")
stud.pos=500,400

stud2=Actor("stud2")
stud2.pos=500,350

score=0
game_over=False

def draw():
    screen.fill("blue")
    emmet.draw()
    stud.draw()
    stud2.draw()
    screen.draw.text("Score= "+str(score),color="cyan",topleft=(10,10))

    if game_over:
        screen.fill("black")
        screen.draw.text("Time's up! Your final score is "+str(score),midtop=(WIDTH/2,10),color="cyan")

def time_up():
    global game_over
    game_over=True

def place_stud():
    stud.x=randint(50,WIDTH-50)
    stud.y=randint(0,HEIGHT-30)

def place_stud2():
    stud2.x=randint(50,WIDTH-50)
    stud2.y=randint(0,HEIGHT-30)

def update():
    global score

    if keyboard.left:
        emmet.x = emmet.x -2
    if keyboard.right:
        emmet.x = emmet.x +2
    if keyboard.up:
        emmet.y = emmet.y -2
    if keyboard.down:
        emmet.y = emmet.y +2

    collect=emmet.colliderect(stud)

    collect2=emmet.colliderect(stud2)

    if collect:
        score=score+10
        place_stud()

    if collect2:
        score=score+10
        place_stud2()

clock.schedule(time_up,60.0)

pgzrun.go()