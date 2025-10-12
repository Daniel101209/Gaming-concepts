import pygame
import random
import sys


pygame.init()


WIDTH, HEIGHT = 400, 600
LANES = [100, 200, 300] 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Dodging Game")


Car=pygame.image.load("Car game/images/car.png")
Car=pygame.transform.scale(Car, (100,80))

Road=pygame.image.load("Car game/images/road.png")
Road = pygame.transform.scale(Road, (WIDTH, HEIGHT))


Hole=pygame.image.load("Car game/images/hole done.png")
Hole=pygame.transform.scale(Hole, (60,40))


clock = pygame.time.Clock()


car_width, car_height = 50, 80
player_lane = 1 
player_y = HEIGHT - car_height - 20


holes = []
hole_width, hole_height = 60, 40
hole_speed = 5


score = 0
font = pygame.font.SysFont(None, 36)

running = True
while running:
    screen.blit(Road,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and player_lane > 0:
                player_lane -= 1
            if event.key == pygame.K_RIGHT and player_lane < 2:
                player_lane += 1

    if random.randint(1, 100) == 1:
        lane = random.choice([0, 1, 2])
        holes.append([LANES[lane] - hole_width//2, -hole_height])

    for h in holes:
        h[1] += hole_speed

    holes = [h for h in holes if h[1] < HEIGHT]

    player_x = LANES[player_lane] - car_width//2
    screen.blit(Car, (player_x, player_y))

    for h in holes:
        screen.blit(Hole, (h[0], h[1]))

        if (player_x < h[0] + hole_width and
            player_x + car_width > h[0] and
            player_y < h[1] + hole_height and
            player_y + car_height > h[1]):
            print("Game Over! Final Score:", score)
            pygame.time.delay(2000)
            pygame.display.update()
            pygame.quit()
            sys.exit()

    score += 1
    score_text = font.render(f"Score: {score}", True, "black")
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)
