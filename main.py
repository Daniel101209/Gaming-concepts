import pgzrun
import random

TITLE = 'Flappy ball'
WIDTH = 800
HEIGHT = 600

r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
CLR = r,g,b

GRAVITY = 2000

class Ball:
    def __init__(self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y
        self.vx = 200
        self.vy = 0
        self.radius = random.randint(20,40)

    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, CLR)


ball = Ball(50, 100)
ball2 = Ball(100, 50)
ball3 = Ball(300, 150)
ball4 = Ball(500, 400)
ball5 = Ball(150,150)

def draw():
    screen.clear()
    ball.draw()
    ball2.draw()
    ball3.draw()
    ball4.draw()
    ball5.draw()

def update(dt):
    uy = ball.vy
    ball.vy += GRAVITY *dt
    ball.y += (uy + ball.vy) *0.5*dt
    
    uy2 = ball2.vy
    ball2.vy += GRAVITY *dt
    ball2.y += (uy2 + ball2.vy) *0.5*dt

    uy3 = ball3.vy
    ball3.vy += GRAVITY *dt
    ball3.y += (uy3 + ball3.vy) *0.5*dt

    uy4 = ball4.vy
    ball4.vy += GRAVITY *dt
    ball4.y += (uy4 + ball4.vy) *0.5*dt

    uy5 = ball5.vy
    ball5.vy += GRAVITY *dt
    ball5.y += (uy5 + ball5.vy) *0.5*dt

    if ball.y > HEIGHT - ball.radius:
        ball.y = HEIGHT - ball.radius
        ball.vy = -ball.vy * 0.9

    ball.x += ball.vx *dt
    if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
        ball.vx = -ball.vx

    if ball2.y > HEIGHT - ball2.radius:
        ball2.y = HEIGHT - ball2.radius
        ball2.vy = -ball2.vy * 0.9

    ball2.x += ball2.vx *dt
    if ball2.x > WIDTH - ball2.radius or ball2.x < ball2.radius:
        ball2.vx = -ball2.vx

    if ball3.y > HEIGHT - ball3.radius:
        ball3.y = HEIGHT - ball3.radius
        ball3.vy = -ball3.vy * 0.9

    ball3.x += ball3.vx *dt
    if ball3.x > WIDTH - ball3.radius or ball3.x < ball3.radius:
        ball3.vx = -ball3.vx

    if ball4.y > HEIGHT - ball4.radius:
        ball4.y = HEIGHT - ball4.radius
        ball4.vy = -ball4.vy * 0.9

    ball4.x += ball4.vx *dt
    if ball4.x > WIDTH - ball4.radius or ball4.x < ball4.radius:
        ball4.vx = -ball4.vx

    if ball5.y > HEIGHT - ball5.radius:
        ball5.y = HEIGHT - ball5.radius
        ball5.vy = -ball5.vy * 0.9

    ball5.x += ball5.vx *dt
    if ball5.x > WIDTH - ball5.radius or ball5.x < ball5.radius:
        ball5.vx = -ball5.vx

def on_key_down(key):
    if key == keys.SPACE:
        ball.vy = -500
        ball2.vy = -600
        ball3.vy = -800
        ball4.vy = -700
        ball5.vy = -550

pgzrun.go()