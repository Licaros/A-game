import pygame, sys
import pygame as pg
import random
pg.init()
print("start")
#windows
screen_width = 800
screen_height = 600
screen = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption("A Game")

#to determine excelleration in Hero.move()
def graph(x, deriv=False):
    if deriv==True:
        return 2*x
    return x^2

class Hero:

    def __init__(self):
        self.x = 10
        self.y = 300
        self.xvel = 0
        self.yvel = 0

        self.xvelmax = 20
        self.xvelmin = -20

        self.image = pg.image.load("C:/Users/Henning/Desktop/Programme/Python/A Game/images/stick.png")


    def move(x, y):
        #input
        self.xvel += x
        self.yvel += y
        print(self.xvel)
    def update(self):
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

        while run == True:
            clock.tick(self.framerate)

            #input
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False

                if event.type == pg.KEYDOWN:
                    if event.type == pg.K_LEFT:
                        player.move(-1,0)
                    if event.type == pg.K_RIGHT:
                        player.move(1,0)

                #if event.type == pg.KEYUP:
                #    if event.type == pg.K_Left:

                #    if event.type == pg.K_Left:

            #draw

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
print("fin")
