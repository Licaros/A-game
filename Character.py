import pygame as pg
from Globals import *

vec = pg.math.Vector2

class Hero(pg.sprite.Sprite):

    def __init__(self, x, y, image):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
        s_player.add(self)
        s_all.add(self)
        self.pos = vec(x, y)
        self.xacc = 0
        self.xvel = 0
        self.yvel = 0
        self.direction = 0
        self.stand = False
    def update(self):
        key = pg.key.get_pressed()

        self.xacc = 0
        if key[pg.K_a] and key[pg.K_d]:
            if self.direction == -1:
                self.xacc += 0.5
            if self.direction == 1:
                self.xacc += -0.5
        elif key[pg.K_a]:
            self.direction = -1
            self.xacc += -0.5
        elif key[pg.K_d]:
            self.direction = 1
            self.xacc += 0.5
        else:
            self.direction = 0
        if key[pg.K_w] and self.stand:
            self.yvel = -10
            self.stand = False

        self.xvel += self.xacc
        self.xvel = self.xvel * PLAYER_FRICTION
        #gravity
        self.yvel += gravity(self.yvel)


        self.pos.x += self.xvel + self.xacc * 0.5
        self.pos.y += self.yvel
        self.rect.midbottom = self.pos
