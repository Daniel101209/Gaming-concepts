import pygame

pygame.init()

WIDTH = 864
HEIGHT = 926

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Flappy Bird")

ground_scroll=0
scroll_speed=4

bg=pygame.image.load("C:/Users/User/Desktop/gaming concepts/PRO GAME DEV/Flappy bird/images/bg (1).png")
ground_img=pygame.image.load("C:/Users/User/Desktop/gaming concepts/PRO GAME DEV/Flappy bird/images/ground.png")

run=True
FPS=60
clock=pygame.time.Clock()

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

    def update(self):
        self.counter=self.counter+1
        flap_cooldown=5

        if self.counter> flap_cooldown:
            self.counter=0
            self.index=self.index+1
            if self.index >= len(self.images):
                self.index=0
        self.images[self.index]

bird_group=pygame.sprite.Group()
flappy=Bird(100,int(HEIGHT/2))
bird_group.add(flappy)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    screen.blit(bg,(0,0))

    bird_group.draw(screen)
    bird_group.update()

    screen.blit(ground_img,(ground_scroll,768))
    ground_scroll=ground_scroll-scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll=0
        
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()