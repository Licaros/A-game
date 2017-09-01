import pygame as pg
from Globals import *

vec = pg.math.Vector2

def collide_solid(subj):
    subj.stand = False
    w = subj.rect.width
    h = subj.rect.height
    subj.rect.x += subj.vel.x + subj.acc.x * subj.friction
    touch = pg.sprite.spritecollide(subj, s_solid, False)
    if touch:
        if subj.vel.x > 0:
            subj.rect.x = touch[0].rect.left - w
        elif subj.vel.x < 0:
            subj.rect.x = touch[0].rect.right
        subj.vel.x = 0
    subj.rect.y += subj.vel.y
    touch = pg.sprite.spritecollide(subj, s_solid, False)
    if touch:
        if subj.vel.y > 0:
            subj.rect.y = touch[0].rect.top - h
            subj.stand = True
        elif subj.vel.y < 0:
            subj.rect.y = touch[0].rect.bottom
        subj.vel.y = 0

class Hero(pg.sprite.Sprite):

    def __init__(self, x, y, image):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        s_alive.add(self)
        s_player.add(self)
        s_all.add(self)
        self.vel = vec(0, 0)
        self.direction = 0
        self.stand = False
        self.energy = 100
        self.friction = 0.9 #speed cap
    def update(self):
        self.acc = vec(0, 0)

        key = pg.key.get_pressed()
        if key[pg.K_a] and key[pg.K_d]:
            if self.direction == -1:
                self.acc.x += 0.5
            if self.direction == 1:
                self.acc.x += -0.5
        elif key[pg.K_a]:
            self.direction = -1
            self.acc.x += -0.5
        elif key[pg.K_d]:
            self.direction = 1
            self.acc.x += 0.5
        #slowdown
        #elif self.acc.x > 0:
        #    self.direction = -1
        else:
            self.acc.x = 0
        if key[pg.K_w] and self.stand:
            self.vel.y = -7 #jump velocity

        self.vel.x = (self.vel.x + self.acc.x) * PLAYER_FRICTION
        #gravity
        self.acc.y = gravity(self.vel.y)
        self.vel.y += self.acc.y
        #colissions and moving
        collide_solid(self)
