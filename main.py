#importing the required modules
import pgzrun
import random
#setting up the size of the screen
WIDTH = 1200
HEIGHT = 600
#Setting up the colors
WHITE=(255,255,255)
BLUE=(0,0,255)
#Importing the charachters
ship= Actor('galaga')
bug=Actor('bug')
#Setting the position and speed of the ship
ship.pos=(WIDTH//2, HEIGHT-60)

speed=5
#Creating the required lists
bullets=[]
enemies=[]
#Creating the nymber if enemies
for x in range(8):
    enemies.append(Actor('bug'))
    enemies[-1].x=100 + 90*x
enemies[-1].y= 80

score=0
direction=1
#Displaying the score
def displayScore():
    screen.draw.text(str(score),(50,30))

#creating the functions for updating and pressing on keys 
def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor('bullet'))
        bullets[-1].x=ship.x
        bullets[-1].y=ship.y - 50

def update():
    global score
    global direction
    moveDown= False

    if keyboard.left:
        ship.x -= speed
        if ship.x <=0:
            ship.x=0
    elif keyboard.right:
        ship.x += speed
        if ship.x >= 1200:
            ship.x=1200
    
    if keyboard.space:
        print("Pressing space")
        bullets.append(Actor('bullet'))
        bullets[-1].x=ship.x
        bullets[-1].y=ship.y
#Creating a function for moving/deleting bullets
    for bullet in bullets:
        if bullet.y <=0:
            bullets.remove(bullet)
        else:
            bullet.y -=10
#Making the enemies move in a row    
    if len (enemies) > 0 and (enemies[-1].x > WIDTH -80 or enemies[0].x < 80):
        moveDown=True
        direction= direction*-1

    for enemy in enemies:
        enemy.x += 5* direction
        if moveDown == True:
            enemy.y += 50
#Making so the bullet gets deleted if it touches the enemy
        for bullet in bullets:
            if enemy.colliderect(bullet):
                score=score+100
                bullets.remove(bullet)
#Drawing everything on the screen
def draw():
    screen.clear()
    screen.fill(BLUE)
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    ship.draw()
    displayScore()


pgzrun.go()