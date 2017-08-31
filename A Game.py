import pygame as pg
from os import path
import random

from Globals import *
from Terrain import *
from Character import *
from Enemy1 import *


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
#relative path to images
dir = path.dirname(__file__)
sticky = path.join(dir, 'images/stick.jpg')
testground = path.join(dir, 'images/ground.jpg')
enemy = path.join(dir, 'images/enemy1.png')

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

    def new(self, level):
        #in process
        lvl = open(level, "r")
        characters = len(lvl.readline())-1
        y = 0
        for i in lvl:
            y += 1
            for j in range(0,characters):
                if i[j] == "P":
                    self.Player = Hero(j*scale, y*scale, sticky)
                elif i[j] == "1":
                    Platform(j*scale, y*scale)

    #Gameloop functions
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                quit()
    def update(self):
        self.Player.update()
        #colissions with enemys
        touch = pg.sprite.spritecollide(self.Player, s_enemy, False)
        if touch:
            touch[0].attack(self.Player)

        #deathzoneaa
        if self.Player.pos.y > HEIGHT+40:
            print("dead")
            self.Player.energy = 0
            pg.quit()
            quit()

        #screen scrolling
        #!!!NEEDS UPDATE (MAP; CAMERA)

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
game.new(path.join(dir,"maps/test1.txt"))
game.execute()



pg.quit()
quit()
print("end")
