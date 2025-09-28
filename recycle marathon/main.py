import pygame
import random
import time

def change_background(img):
    background=pygame.image.load(img)
    bg=pygame.transform.scale(background,(screen_width,screen_height))
    screen.blit(bg,(0,0))

pygame.init()
screen_width=900
screen_height=700

screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Recycle Marathon")

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:/Users/User/Desktop/gaming concepts/PRO GAME DEV/recycle marathon/bin.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(40,60))
        self.rect=self.image.get_rect()

class Recyclable(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load(img).convert_alpha()
        self.image=pygame.transform.scale(self.image,(30,30))
        self.rect=self.image.get_rect() 


class Non_Recyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:/Users/User/Desktop/gaming concepts/PRO GAME DEV/recycle marathon/plastic.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(40,60))
        self.rect=self.image.get_rect()

images=["recycle marathon/item1.png","recycle marathon/item2.png","recycle marathon/item3.png"]

item_list=pygame.sprite.Group()
allsprites=pygame.sprite.Group()
plastic_list=pygame.sprite.Group()

for i in range(50):
    item=Recyclable(random.choice(images))
    item.rect.x=random.randrange(screen_width)
    item.rect.y=random.randrange(screen_height)
    item_list.add(item)
    allsprites.add(item)

for i in range(20):
    plastic=Non_Recyclable()
    plastic.rect.x=random.randrange(screen_width)
    plastic.rect.y=random.randrange(screen_height)
    plastic_list.add(plastic)
    allsprites.add(plastic)

bin=Bin()
allsprites.add(bin)

playing=True
score=0
clock=pygame.time.Clock()
start_time=time.time()

font=pygame.font.SysFont("Comic Snas MS",22)
text=font.render("Score="+str(score),True,"White")

while playing:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing=False
    
    timeElapsed=time.time()-start_time
    if timeElapsed >= 60:
        if score > 50:
            text=font.render(" Bin loot successful ",True,"red")
            change_background("")
        else:
            text=font.render(" Better luck next time ",True,"red")
            change_background("")
    else:
        change_background("recycle marathon/bground.png")
        countDown=font.render("Time left: "+str(60-int(timeElapsed)),True,"white")
        screen.blit(countDown,(20,10))

    pygame.display.flip()

pygame.quit()