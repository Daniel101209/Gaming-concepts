import pygame
import time

pygame.init()

WIDTH=800
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Father's day Greeting card")

image=pygame.image.load("C:/Users/User/Desktop/gaming concepts/PRO GAME DEV/father's day/images/father's day card 1.jpg")
image=pygame.transform.scale(image,(WIDTH,HEIGHT))

gameloop = True
while (gameloop):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop=False
    
    font=pygame.font.SysFont("Comic Sans MS",50)
    font1=pygame.font.SysFont("Comic Sans MS",30)
    t1=font.render("Happy",True,"red")
    t2=font.render("Father's day!",True,"red")
    screen.blit(image,(0,0))
    screen.blit(t1,(280,250))
    screen.blit(t2,(280,330))
    pygame.display.update()
    time.sleep(2)

    image2=pygame.image.load("C:/Users/User/Desktop/gaming concepts/PRO GAME DEV/father's day/images/father's day card 2.jpg")
    image2=pygame.transform.scale(image2,(WIDTH,HEIGHT))

    t3=font.render("To the best father in the world!",True,"red")
    screen.fill("white")
    screen.blit(image2,(0,0))
    screen.blit(t3,(30,200))
    pygame.display.update()
    time.sleep(2)

    image3=pygame.image.load("C:/Users/User/Desktop/gaming concepts/PRO GAME DEV/father's day/images/father's day card 3.jpg")
    image3=pygame.transform.scale(image3,(WIDTH,HEIGHT))

    t4=font1.render("Wish you always be the same and amazing as you are!",True,"red")
    screen.fill("white")
    screen.blit(image3,(0,0))
    screen.blit(t4,(30,200))
    pygame.display.update()
    time.sleep(2)
 
pygame.quit()