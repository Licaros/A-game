import pygame as pg
from Globals import *

class Platform(pg.sprite.Sprite):

    def __init__(self, x, y):
        super(Platform, self).__init__()
        self.image = pg.Surface((scale,scale))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        s_solid.add(self)
        s_all.add(self)
        self.pos = self.rect.midtop

class Spike(pg.sprite.Sprite):

    def __init__(self, x, y, image):
        super(Spike, self).__init__()
        self.x = x
        self.y = y
        self.image  = pg.image.load(image).convert_alpha()
        self.rect = pg.Rect((self.x,self.y),(10,10))
