import pygame

pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Understanding OOP")

class Rect():
    def __init__(self,color,dimensions):
        self.place=screen
        self.c=color
        self.dim=dimensions

    def draw(self):
        self.draw_rect=pygame.draw.rect(self.place,self.c,self.dim)

r1=Rect("red",(90,30,300,300))
r1.draw()

r2=Rect("blue",(40,120,0,0))
r2.draw()

pygame.display.update()