import pgzrun
from random import randint

WIDTH=400
HEIGHT=400

witch=Actor('witch')
witch.pos=200,200
poition=Actor('poition')
poition.pos=100,200


def draw():   
    screen.blit('night forest',(0,0))
    witch.draw()
    poition.draw()

def update():
    if keyboard.up:
        witch.y = witch.y - 3
    if keyboard.down:
        witch.y = witch.y + 3
    if keyboard.right:
        witch.x = witch.x + 3
    if keyboard.left:
        witch.x = witch.x - 3

def select_target():
    global position
    target_x = randint(50,WIDTH-50)
    target_y = randint(50,HEIGHT-50)
    position=(target_x,target_y)

def move_poition():
    global position
    if witch.colliderect(poition):
        animate(poition,"bounce_end",duration=1,pos=next(position))
        screen.draw.text("You won!",color="red",center=(100,100))

move_poition()
update()
pgzrun.go()