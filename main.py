#Importing the needed modules
import pygame

pygame.init()
#Setting up the screen
screen=pygame.display.set_mode((600,600))
screen.fill((255,255,255))

blue=(0,0,255)

pygame.display.update()
#Creating the class for circles
class Circle():
    def __init__(self,color,pos,radius,width):
        self.circle_color=color
        self.circle_pos=pos
        self.circle_radius=radius
        self.circle_width=width
        self.circle_surface=screen
#Creating the circle
    def draw(self):
        self.Draw_circle=pygame.draw.circle(self.circle_surface,self.circle_color,self.circle_pos,self.circle_radius,self.circle_width)
#Creating the function for the circle to gorw 
    def grow(self,r):
        self.circle_radius=self.circle_radius+r
        self.Draw_circle=pygame.draw.circle(self.circle_surface,self.circle_color,self.circle_pos,self.circle_radius,self.circle_width)
#Selecting the color for the circle
circle=Circle(blue,(300,300),25,0)
circle2=Circle("orange",(200,200),10,0)
circle3=Circle("green",(400,400),5,0)
#Creating the while loop that will react to mouse clicking and activating the grow function
while 1:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255,255,255))
            circle.draw()
            circle2.draw()
            circle2.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill((255,255,255))
            circle.grow(20)
            circle2.grow(8)
            circle3.grow(4)
            pygame.display.update()

