import pygame

pygame.init()

screen=pygame.display.set_mode((900,500))
pygame.display.set_caption("Space game")

background = pygame.image.load("C:/Users/User/Desktop/gaming concepts/PRO GAME DEV/space game/galaxy.jpg")
background=pygame.transform.scale(background,(900,500))

x= 450
player_ship=pygame.image.load("C:/Users/User/Desktop/gaming concepts/PRO GAME DEV/space game/spaceship.png")
player_ship=pygame.transform.scale(player_ship,(100,100))

gameloop=True
FPS=60
clock=pygame.time.Clock()

while gameloop:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            gameloop = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x=x-3
        elif event.key == pygame.K_RIGHT:
            x=x+3

    screen.blit(background,(0,0))
    screen.blit(player_ship,(x,400))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()