import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 255))

blue = (0, 0, 255)

pygame.display.update()

class Rectangle():
    def __init__(self, color, pos, height, width):
        self.rect_color = color
        self.rect_pos = pos
        self.rect_height = height
        self.rect_width = width
        self.rect_surface = screen

    def draw(self):
        pygame.draw.rect(self.rect_surface, self.rect_color, 
                         (self.rect_pos[0], self.rect_pos[1], self.rect_width, self.rect_height))

    def grow(self, r):
        self.rect_height += r
        pygame.draw.rect(self.rect_surface, self.rect_color, 
                         (self.rect_pos[0], self.rect_pos[1], self.rect_width, self.rect_height))

rect = Rectangle(blue, (300, 300), 30, 80)
rect2 = Rectangle((255, 165, 0), (200, 200), 15, 60)
rect3 = Rectangle((0, 255, 0), (400, 400), 45, 50)
rect4 = Rectangle((0, 255, 255), (150, 150), 20, 70)

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255, 255, 255))
            rect.draw()
            rect2.draw()
            rect3.draw()
            rect4.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill((255, 255, 255))
            rect.grow(20)
            rect2.grow(8)
            rect3.grow(4)
            rect4.grow(2)
            pygame.display.update()