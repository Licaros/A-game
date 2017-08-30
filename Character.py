import pygame as pg
from Globals import *

vec = pg.math.Vector2

def collide_solid(subj):
    touch = pg.sprite.spritecollide(subj, s_solid, False)
    if touch:
        subj.pos.y = touch[0].rect.y -10
        subj.vel.y = 0
        subj.stand = True
    else:
        subj.stand = False

    subj.pos.x += subj.vel.x + subj.acc.x * 0.5
    subj.pos.y += subj.vel.y
    subj.rect.center = subj.pos

class Hero(pg.sprite.Sprite):

    def __init__(self, x, y, image):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        s_alive.add(self)
        s_player.add(self)
        s_all.add(self)
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.direction = 0
        self.stand = False
        self.energy = 100
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
        else:
            self.direction = 0
        if key[pg.K_w] and self.stand:
            self.vel.y = -7

        self.vel.x += self.acc.x
        self.vel.x = self.vel.x * PLAYER_FRICTION
        #gravity
        self.acc.y = gravity(self.vel.y)
        self.vel.y += self.acc.y
        #colissions and moving
        collide_solid(self)

        self.pos.x += self.vel.x + self.acc.x * 0.5
        self.pos.y += self.vel.y
        self.rect.center = self.pos
