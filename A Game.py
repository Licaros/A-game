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

img_player = path.join(dir, 'images/Walker.png')
#__main()__
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
                    self.Player = Hero(j*scale, y*scale, img_player)
                elif i[j] == "1":
                    Platform(j*scale, y*scale)

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
        if self.Player.rect.y > HEIGHT+40:
            print("dead")
            self.Player.energy = 0
            pg.quit()
            quit()

        #screen scrolling
        #!!!NEEDS UPDATE (MAP; CAMERA)

        s_all.update()

    def draw(self):
        screen.fill((200,200,200))

        s_all.draw(screen)
        screen.blit(self.label, (10, 10))
        screen.blit(self.speedmeter, (10, 25))
        screen.blit(self.accel, (10, 40))
        pg.display.update()

    def execute(self):
        clock = pg.time.Clock()
        run = True
        #main loop
        while run == True:
            clock.tick(framerate)
            try:
                tack += 1
            except:
                tack = 20
            if tack == 20:
                tack= 0
                self.label = font.render("fps: " + str(clock.get_fps()), True, (255,0,0))
                self.speedmeter = font.render("Speed: " + str(self.Player.vel.x), True, (255, 0, 0))
                self.accel = font.render("Acceleration: " + str(self.Player.acc.x), True, (255, 0, 0))
            self.events()
            self.update()
            self.draw()


game = Game()
game.new(path.join(dir,"maps/test1.txt"))
game.execute()



pg.quit()
quit()
print("end")
