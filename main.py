import pgzrun
import random

WIDTH = 1200
HEIGHT = 600

WHITE=(255,255,255)
BLUE=(255,0,0)

main_character= Actor('emmet')
villan=Actor('robot')

main_character.pos=(WIDTH//2, HEIGHT-60)

speed=5

bullets=[]
enemies=[]

enemies.append(Actor('robot'))
enemies[-1].x=10
enemies[-1].y=-100

score=0

def displayScore():
    screen.draw.text(str(score),(50,30))

def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor('stud'))
        bullets[-1].x=main_character.x
        bullets[-1].y=main_character.y - 50

def update():
    global score
    if keyboard.left:
        main_character.x -= speed
        if main_character.x <=0:
            main_character.x=0
    elif keyboard.right:
        main_character.x += speed
        if main_character.x >= 1200:
            main_character.x=1200
    if keyboard.space:
        print("Pressing space")
        bullets.append(Actor('stud'))
        bullets[-1].x=main_character.x
        bullets[-1].y=main_character.y

    for stud in bullets:
        if stud.y <=0:
            bullets.remove(stud)
        else:
            stud.y -=10
    
    for enemy in enemies:
        enemy.y +=5

        if enemy.y >= HEIGHT:
            enemy.y= -100
            enemy.x=random.randint(50,WIDTH-50)

        for stud in bullets:
            if enemy.colliderect(stud):
                score=score+100
                bullets.remove(stud)
                enemies.remove(enemy)

def draw():
    screen.clear()
    screen.fill(BLUE)
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    displayScore()

pgzrun.go()