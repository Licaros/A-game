import pygame as pg
from os import path
import random

from Globals import *
from Terrain import *
from Character import *
from Strawman import *
from Knight import *


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREEN)
#relative path to images
dir = path.dirname(__file__)

img_player = path.join(dir, 'images\walker.png')
img_strawman = path.join(dir, 'images\strawman.png')
img_knight = path.join(dir, 'images\knight.png')
#__main()__
class Game:

    def __init__(self):
        pg.init()

    def new(self, level):
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
                elif i[j] == "K":
                    Knight(j*scale, y*scale, img_knight)
        self.camera = Camera(WIDTH, HEIGHT)

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
        if self.Player.rect.y > HEIGHT+1000: #deathzone
            print("dead")
            self.Player.energy = 0
            pg.quit()
            quit()

        s_all.update()
        self.camera.update(self.Player)

    def draw(self):
        screen.fill((00,00,00))

        for sprite in s_all:
            screen.blit(sprite.image, self.camera.apply(sprite))

        #hitboxes
        for sprite in s_alive:
            drawrect = self.camera.applyr(sprite.rect)
            pg.draw.rect(screen, (255,0,0), drawrect, 2)
        for sprite in s_alive:
            try:
                drawrect = self.camera.applyr(sprite.sensor)
                pg.draw.rect(screen, (255,255,0), drawrect,2)
            except:
                1+1
        #pg.draw.rect(screen, (255,0,0), [100,100,100,100], 2)
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

class Map:

    def __init__(level):
        self.dict = "{01: Hero(), 02: Knight()}"



class Camera:

    def __init__(self, width, height):
        self.rect = pg.Rect(0,0,width,height)
        self.width = width
        self.height = height

    def apply(self, target):
        return target.rect.move(self.rect.topleft)

    def applyr(self, rec):
        return rec.move(self.rect.topleft)

    def update(self, target):
        x = self.rect.x
        y = self.rect.y
        tx = target.rect.x
        ty = target.rect.y

        x = (self.width/2) - target.rect.x
        y = (self.height/2) - target.rect.y
        self.rect = pg.Rect(x,y,self.width,self.height)

game = Game()
game.new(path.join(dir,"maps/test1.txt"))

#main
game.execute()

pg.quit()
quit()
print("end")
