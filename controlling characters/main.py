import pygame
pygame.init()

WIDTH=700
HEIGHT=500

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Rocket in Space")
bg=pygame.image.load(("C:/Users/User/Desktop/gaming concepts/PRO GAME DEV/controlling characters/galaxy.jpg"))
bg=pygame.transform.scale(bg,(700,500))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:/Users/User/Desktop/gaming concepts/PRO GAME DEV/controlling characters/rocket.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(70,100))
        self.rect=self.image.get_rect()
    
    def update(self,pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0,-1)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0,1)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-1,0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(1,0)
        
        if self.rect.left<0:
            self.rect.left=0
        elif self.rect.right>700:
            self.rect.right=700
        if self.rect.top<0:
            self.rect.top=0
        elif self.rect.bottom>500:
            self.rect.bottom=500

sprites=pygame.sprite.Group()

def Start_game():
    player=Player()
    sprites.add(player)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)
        pressed_keys =pygame.key.get_pressed()
        player.update(pressed_keys)
        screen.blit(bg,(0,0))
        sprites.draw(screen)
        pygame.display.update()

Start_game()
        