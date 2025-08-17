import pygame

pygame.init()

screen=pygame.display.set_mode((900,500))
pygame.display.set_caption("Space game")

background = pygame.image.load("C:/Users/User/Desktop/gaming concepts/PRO GAME DEV/space game/galaxy.jpg")
background=pygame.transform.scale(background,(900,500))

x= 450
player_ship=pygame.image.load("C:/Users/User/Desktop/gaming concepts/PRO GAME DEV/space game/spaceship.png")
player_ship=pygame.transform.scale(player_ship,(100,100))

x1= 450
spaceship2 = pygame.image.load("C:/Users/User/Desktop/gaming concepts/PRO GAME DEV/space game/spaceship2.png")
spaceship2=pygame.transform.rotate(spaceship2,180)
spaceship2=pygame.transform.scale(spaceship2,(100,100))
spaceship2_rect=spaceship2.get_rect(center=(x1,10))

bullet=pygame.image.load("C:/Users/User/Desktop/gaming concepts/PRO GAME DEV/space game/bullet.png")
bullet=pygame.transform.scale(bullet,(30,30))
bullet=pygame.transform.rotate(bullet,-90)

bullets = []

gameloop=True
FPS=60
clock=pygame.time.Clock()

while gameloop:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            gameloop = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and x > 0:
            x=x-3
        elif event.key == pygame.K_RIGHT and x < 800:
            x=x+3
        
    keys=pygame.key.get_pressed()
    if keys[pygame.K_a] and x1 > 0:
        x1=x1-3
    if keys[pygame.K_d] and x1 < 800:
        x1=x1+3

    if keys[pygame.K_SPACE]:
        bullet_rect=bullet.get_rect(center=spaceship2_rect.midtop)
        bullets.append({"rect":bullet_rect})
    for b in bullets:
        b["rect"].y=b["rect"].y+5


    screen.blit(background,(0,0))
    screen.blit(player_ship,(x,400))
    screen.blit(spaceship2,(x1,10))
    for b in bullets:
        screen.blit(bullet,b["rect"])
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()