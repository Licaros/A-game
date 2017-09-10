import pygame as pg
from os import path
import random

from Globals import *
from Terrain import *
from Character import *
from Enemy import *


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREEN)
#relative path to images
dir = path.dirname(__file__)

img_player = path.join(dir, 'images\walker.png')
img_strawman = path.join(dir, 'images\strawman.png')
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
                elif i[j] == "S":
                    Strawman(j*scale, y*scale, img_strawman)
                elif i[j] == "A":
                    Race(j*scale, y*scale)
                elif i[j] == "B":
                    Race(j*scale, y*scale, True)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.run = False

        key = pg.key.get_pressed()
        if key[pg.K_ESCAPE]:
            self.run = False
            pg.quit()
            quit()


    def update(self):
        for sprite in s_alive:
            sprite.update()
        for sprite in s_solid:
            try:
                sprite.update()
            except:
                pass

        #deathzone
        if self.Player.rect.y > HEIGHT+40:
            print("dead")
            self.Player.energy = 0
            pg.quit()
            quit()

        s_all.update()

    def draw(self):
        screen.fill((00,00,00))

        s_solid.draw(screen)
        s_enemy.draw(screen)
        s_player.draw(screen)
        screen.blit(self.label, (10, 10))
        screen.blit(self.speedmeter, (10, 25))
        screen.blit(self.accel, (10, 40))
        pg.display.update()

    def execute(self):
        clock = pg.time.Clock()
        self.run = True
        #main loop
        while self.run == True:
            clock.tick(framerate)
            try:
                tack += 1
            except:
                tack = 10
            if tack == 10:
                tack= 0
                self.label = font.render("fps: " + str(round(clock.get_fps(),1)), True, (255,0,0))
                self.speedmeter = font.render("Speed: " + str(self.Player.vel.x), True, (255, 0, 0))
                self.accel = font.render("Acceleration: " + str(self.Player.acc.x), True, (255, 0, 0))
            self.events()
            self.update()
            self.draw()


game = Game()
game.new(path.join(dir,"maps/test1.txt"))

#main
while 1:
    game.execute()



pg.quit()
quit()
print("end")
