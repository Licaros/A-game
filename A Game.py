import pygame as pg
from os import path
import random

import Character
import Terrain



pg.init()
print("start")

#windows
screen_width = 800
screen_height = 600
screen = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption("A Game")

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

#sprite groups
s_player = pg.sprite.Group()
s_enemy  = pg.sprite.Group()
s_solid  = pg.sprite.Group()



g = Terrain.Ground(testground, s_solid)
Player = Character.Hero(sticky, s_player)

class Game:

    def __init__(self):
        scl=10
        pg.init()
        self.framerate = 30

    def execute(self):
        clock = pg.time.Clock()
        run = True
        pg.event.get()

        #main loop
        while run == True:
            clock.tick(self.framerate)
            #input
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
            Player.move()

            Player.colission(g)

            #pg.sprite.spritecollideany(s_player, s_solid)

            #background
            screen.fill((105,105,105))
            Player.show(screen)
            g.show(screen)
            pg.display.update()
game = Game()






game.execute()






pg.quit()
quit()
print("end")
