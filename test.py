import pgzrun

WIDTH=400
HEIGHT=400

witch=Actor('witch')
witch.pos=200,200
poition=Actor('poition')
poition.pos=100,200
def draw():   
    screen.blit('night forest',(0,0))
    witch.draw()
    poition.draw()
pgzrun.go()