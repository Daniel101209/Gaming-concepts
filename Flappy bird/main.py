#importing the required modules
import pygame
import random
#initialising
pygame.init()
#setting up the screen and caption
WIDTH = 864
HEIGHT = 926

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Flappy Bird")
#setting up the movement speed
ground_scroll=0
scroll_speed=4
flying=False
game_over=False
pipe_gap= 150
pipe_frequency=1500
last_pipe= pygame.time.get_ticks()-pipe_frequency
#loading the images for the background and ground
bg=pygame.image.load("C:/Users/User/Desktop/gaming concepts/PRO GAME DEV/Flappy bird/images/bg (1).png")
ground_img=pygame.image.load("C:/Users/User/Desktop/gaming concepts/PRO GAME DEV/Flappy bird/images/ground.png")

run=True
FPS=60
clock=pygame.time.Clock()
#creating the bird class
class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.images=[]
        self.index=0
        self.counter=0
        for num in range(1,4):
            img=pygame.image.load(f'C:/Users/User/Desktop/gaming concepts/PRO GAME DEV/Flappy bird/images/bird{num}.png')
            self.images.append(img)
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
        self.vel=0
        self.clicked=False
#creating the updating function
    def update(self):
        if flying ==True:
            self.vel=self.vel + 0.5
            if self.vel>8:
                self.vel=8
            if self.rect.bottom <768:
                self.rect.y=self.rect.y+int(self.vel)

        if game_over==False:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked==False:
                self.clicked=True
                self.vel=-10
            if pygame.mouse.get_pressed()[0] == 0 and self.clicked == False:
                self.clicked=False

            self.counter=self.counter+1
            flap_cooldown=5

            if self.counter> flap_cooldown:
                self.counter=0
                self.index=self.index+1
                if self.index >= len(self.images):
                    self.index=0
            self.images[self.index]

            self.image=pygame.transform.rotate(self.images[self.index], self.vel*-2)
        else:
            self.image=pygame.transform.rotate(self.images[self.index],-90)
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x,y,position):
        super().__init__()
        self.image=pygame.image.load("C:/Users/User/Desktop/gaming concepts/PRO GAME DEV/Flappy bird/images/pipe.png")
        self.rect=self.image.get_rect()
        if position == 1:
            self.image == pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft=[x,y-int(pipe_gap/2)]
        if position == -1:
            self.rect.topleft=[x,y+int(pipe_gap/2)]
    
    def update(self):
        self.rect.x = self.rect.x - scroll_speed
        if self.rect.right < 0:
            self.kill()

#adding the elements
bird_group=pygame.sprite.Group()
pipe_group=pygame.sprite.Group()

flappy=Bird(100,int(HEIGHT/2))
bird_group.add(flappy)
#adding the event for game start
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying =True

#adding the images to the game
    screen.blit(bg,(0,0))

    bird_group.draw(screen)
    bird_group.update()

    pipe_group.draw(screen)

    screen.blit(ground_img,(ground_scroll,768))

    if pygame.sprite.groupcollide(bird_group,pipe_group,False,False) or flappy.rect.top < 0:
        game_over = True

    if flappy.rect.bottom > 768:
        game_over = True
        flying = False
    
    if game_over == False:
        ground_scroll=ground_scroll-scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll=0
            
#setting the speed for updating the screen
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()