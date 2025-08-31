import pygame

pygame.init()

screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Match it!")

subway_surfers=pygame.image.load("C:/Users/User/Desktop/gaming concepts/PRO GAME DEV/match the following/subway surfers.png")
candy_crush=pygame.image.load("C:/Users/User/Desktop/gaming concepts/PRO GAME DEV/match the following/candy crush.png")
cut_the_rope=pygame.image.load("C:/Users/User/Desktop/gaming concepts/PRO GAME DEV/match the following/cut the rope.png")
angry_birds=pygame.image.load("C:/Users/User/Desktop/gaming concepts/PRO GAME DEV/match the following/angry birds.png")
roblox=pygame.image.load("C:/Users/User/Desktop/gaming concepts/PRO GAME DEV/match the following/roblox.png")
minecraft=pygame.image.load("C:/Users/User/Desktop/gaming concepts/PRO GAME DEV/match the following/minecraft.png")

subway_surfers = pygame.transform.scale(subway_surfers,(100,100))
candy_crush = pygame.transform.scale(candy_crush,(100,100))
cut_the_rope = pygame.transform.scale(cut_the_rope,(100,100))
angry_birds = pygame.transform.scale(angry_birds,(100,100))
roblox = pygame.transform.scale(roblox,(135,100))
minecraft = pygame.transform.scale(minecraft,(100,100))

f=pygame.font.SysFont("Comic Sans MS",36)

text1=f.render("Subway Surfers",True,"white")
text2=f.render("Candy Crush",True,"white")
text3=f.render("Cut The Rope",True,"white")
text4=f.render("Angry Birds",True,"white")
text5=f.render("Roblox",True,"white")
text6=f.render("Minecraft",True,"white")

gameloop = True

while gameloop:
    screen.fill("Black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop=False

        screen.blit(subway_surfers,(150,205))
        screen.blit(candy_crush,(150,5))
        screen.blit(cut_the_rope,(150,305))
        screen.blit(angry_birds,(150,105))
        screen.blit(roblox,(135,505))
        screen.blit(minecraft,(150,405))

        screen.blit(text1,(300,50))
        screen.blit(text2,(300,150))
        screen.blit(text3,(300,250))
        screen.blit(text4,(300,350))
        screen.blit(text5,(300,450))
        screen.blit(text6,(300,550))

    
        if event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            pygame.draw.circle(screen,"cyan",(pos),20,0)
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            pos2=pygame.mouse.get_pos()
            pygame.draw.line(screen,"hotpink",(pos),(pos2),5)
            pygame.draw.circle(screen,"cyan",(pos2),20,0)
            pygame.display.update()
        pygame.display.update()
pygame.quit()