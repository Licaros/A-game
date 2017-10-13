import pygame as pg
from Globals import *

class Platform(pg.sprite.Sprite):

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((scale,scale))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        s_solid.add(self)
        s_all.add(self)
        self.pos = self.rect.midtop

class Race(pg.sprite.Sprite):

    def __init__(self, x, y, Fin=False):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((scale, 40))
        self.image.fill((0,255,255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.fin = Fin
        s_all.add(self)

    def update(self):
        global timerstart
        global timer
        if self.fin and pg.sprite.spritecollide(self, s_player, False) and timer > 2:
            ("Fin: " + str(timer))

            timer = 0
        elif not self.fin and pg.sprite.spritecollide(self, s_player, False):
            timerstart = True

        if timerstart:
            timer+=1
class Spike(pg.sprite.Sprite):

    def __init__(self, x, y, image):
        super(Spike, self).__init__()
        self.x = x
        self.y = y
        self.image  = pg.image.load(image).convert_alpha()
        self.rect = pg.Rect((self.x,self.y),(10,10))
