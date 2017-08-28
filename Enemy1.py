import pygame as pg
from Globals import *

vec = pg.math.Vector2

class Enemy(pg.sprite.Sprite):

    def __init__(self, x, y, image):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
        s_alive.add(self)
        s_enemy.add(self)
        s_all.add(self)
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.direction = 0
        self.stand = False
        self.energy = 100
    def update(self):
        self.acc = vec(0, 0)

        self.vel.x += self.acc.x
        self.vel.x = self.vel.x * PLAYER_FRICTION
        #gravity
        self.acc.y = gravity(self.vel.y)
        self.vel.y += self.acc.y
        #position update
        self.pos.x += self.vel.x + self.acc.x * 0.5
        self.pos.y += self.vel.y
        self.rect.midbottom = self.pos
