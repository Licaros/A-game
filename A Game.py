import pygame as pg
from os import path
import random

from Globals import *
from Terrain import *
from Character import *


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
#relative path to images
dir = path.dirname(__file__)
sticky = path.join(dir, 'images/stick.jpg')
testground = path.join(dir, 'images/ground.jpg')

#to determine excelleration
#!! not implemented
def graph(x, deriv=False):
    if deriv==True:
        return 2*x
    return x**2

#__main()__
class Game:

    def __init__(self):
        pg.init()

    def new(self): #level etc.
        self.Player = Hero(30, 0, sticky)
        self.Ground = Platform(0, HEIGHT-10, WIDTH, HEIGHT)

    #Gameloop functions
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                quit()
    def update(self):
        self.Player.update()
        #colission
        touch = pg.sprite.spritecollide(self.Player, s_solid, False)
        if touch:
            self.Player.pos.y = touch[0].y + 1
            self.Player.yvel = 0
            self.Player.stand = True

        #death
        if self.Player.pos.y > HEIGHT+1:
            print("dead")
            pg.quit()
            quit()
        s_all.update()
    def draw(self):
        screen.fill((80,70,160))
        s_all.draw(screen)
        pg.display.update()

    def execute(self):
        clock = pg.time.Clock()
        run = True
        #main loop
        while run == True:
            clock.tick(framerate)
            self.events()
            self.update()
            self.draw()


game = Game()
game.new()
game.execute()



pg.quit()
quit()
print("end")
