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
        self.radius = 40

    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, CLR)

ball = Ball(50, 100)

def draw():
    screen.clear()
    ball.draw()

def update(dt):
    uy = ball.vy
    ball.vy += GRAVITY *dt
    ball.y += (uy + ball.vy) *0.5*dt

    if ball.y > HEIGHT - ball.radius:
        ball.y = HEIGHT - ball.radius
        ball.vy = -ball.vy * 0.9

    ball.x += ball.vx *dt
    if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
        ball.vx = -ball.vx

def on_key_down(key):
    if key == keys.SPACE:
        ball.vy = -500

pgzrun.go()

