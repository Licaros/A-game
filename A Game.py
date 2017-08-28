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

#__main()__a
class Game:

    def __init__(self):
        pg.init()

    def new(self): #level etc.
        self.Player = Hero(400, 100, sticky)
        self.Ground = Platform(0, HEIGHT-100, 100, 20)
        self.Plat1 = Platform(500, HEIGHT-150, 100, 20)
        self.Plat2 = Platform(0, HEIGHT-10, 1000, 20)
    #Gameloop functions
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                quit()
    def update(self):
        self.Player.update()
        #colissiona
        touch = pg.sprite.spritecollide(self.Player, s_solid, False)
        if touch:
            self.Player.pos.y = touch[0].rect.y + 1
            self.Player.vel.y = 0
            self.Player.stand = True

        #deathzone
        if self.Player.pos.y > HEIGHT+40:
            print("dead")
            pg.quit()
            quit()

        #screen scrollingddd
        xcorrecture = -(self.Player.vel.x + self.Player.acc.x * 0.5)
        ycorrecture = -(self.Player.vel.y + self.Player.acc.y * 0.5)
        if self.Player.pos.x > WIDTH - 200:
            self.Player.pos.x = WIDTH - 200
            for i in s_solid:
                i.rect.x += xcorrecture
        elif self.Player.pos.x < 200:
            self.Player.pos.x = 200
            for i in s_solid:
                i.rect.x += xcorrecture
        if self.Player.pos.y < 200:
            self.Player.pos.y = 200
            for i in s_solid:
                i.rect.y += ycorrecture
        elif self.Player.pos.y > HEIGHT - 200:
            self.Player.pos.y = HEIGHT - 200
            for i in s_solid:
                i.rect.y += ycorrecture
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
