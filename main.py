import pgzrun
import random

WIDTH = 1200
HEIGHT = 600

WHITE=(255,255,255)
RED=(255,0,0)

main_character= Actor('emmet')
robot=Actor('robot')

main_character.pos=(WIDTH//2, HEIGHT-60)

speed=5

bullets=[]
enemies=[]

for x in range(8):
    enemies.append(Actor('robot'))
    enemies[-1].x=100 + 90*x
enemies[-1].y= 80

score=0
direction=1

def displayScore():
    screen.draw.text(str(score),(50,30))
 
def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor('stud'))
        bullets[-1].x=main_character.x
        bullets[-1].y=main_character.y - 50

def update():
    global score
    global direction
    moveDown= False

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

    for bullet in bullets:
        if bullet.y <=0:
            bullets.remove(bullet)
        else:
            bullet.y -=10
    
    if len (enemies) > 0 and (enemies[-1].x > WIDTH -80 or enemies[0].x < 80):
        moveDown=True
        direction= direction*-1

    for enemy in enemies:
        enemy.x += 5* direction
        if moveDown == True:
            enemy.y += 50

        for bullet in bullets:
            if enemy.colliderect(bullet):
                score=score+100
                bullets.remove(bullet)

def draw():
    screen.clear()
    screen.fill(RED)
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    main_character.draw()
    displayScore()


pgzrun.go()