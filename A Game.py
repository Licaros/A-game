import sys
import pygame as pg
import os
import random

pg.init()
print("start")

#windows
screen_width = 800
screen_height = 600
screen = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption("A Game")

#relative path to images
dir = os.path.dirname(__file__)
sticky = os.path.join(dir, 'images/stick.jpg')

#to determine excelleration
#!! not implemented
def graph(x, deriv=False):
    if deriv==True:
        return 2*x
    return x**2

class Hero(pg.sprite.Sprite):

    def __init__(self):
        self.image = pg.image.load(sticky)


        self.x = 10
        self.y = 300

        self.right = False
        self.left = False
        self.xvel = 0
        self.yvel = 0
        self.xvelmax = 10
        self.xvelmin = -10

    def update(self):
        #movement input
        #!! -Feature: hält man Right gedrückt und dann Left+Right gedrückt wird der
        #!!           neue Input (Left) akeptiert (man dreht sich)
        #!!           erlaubt schnelle Rektionen (Keine "Blockade")
        if self.right:
            self.xvel += 1

        if self.left:
            self.xvel -= 1

        #friction on X Axcis
        if not self.left and not self.right and self.yvel == 0:
            #!! möglicherweise eine Funktion einbauen, damit das Movement
            #!! natürlicher wird
            if self.xvel > 0:
                self.xvel += -1
            elif self.xvel < 0:
                self.xvel += 1

        #speedcap
        if self.xvel > self.xvelmax:
            self.xvel=self.xvelmax
        elif self.xvel < self.xvelmin:
            self.xvel=self.xvelmin

        #updateing coordinates
        self.x += self.xvel
        self.y += self.yvel

    def show(self):
        screen.blit(self.image,(self.x,self.y))

Player = Hero()

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
            events = list(pg.event.get())
            for event in events:
                if event.type == pg.QUIT:
                    run = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        Player.left = True
                    if event.key == pg.K_RIGHT:
                        Player.right = True

                if event.type == pg.KEYUP:
                    if event.key == pg.K_LEFT:
                        Player.left = False
                    if event.key == pg.K_RIGHT:
                        Player.right = False

            #background
            screen.fill((255,255,255))

            #sprites
            Player.update()

            Player.show()

            pg.display.update()


game = Game()
game.execute()




pg.quit()
quit()
print("end")
