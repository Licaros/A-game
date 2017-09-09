import pygame as pg
from Globals import *

vec = pg.math.Vector2

def collide_solid(subj):
    subj.stand = False
    w = subj.rect.width
    h = subj.rect.height
    subj.rect.x += (subj.vel.x + subj.acc.x) * subj.friction
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
        self.images = slice_spritesheet(image, 20*4, 20*4 )
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        s_alive.add(self)
        s_player.add(self)
        s_all.add(self)

        self.vel = vec(0, 0)
        self.direction = 1
        self.stand = False

        self.energy = 100
        self.speed = 0.4
        self.jumpheight = -6
        self.friction = 0.85 #speed cap
        self.acc = vec(0,0)
        self.anim_tick = 0
        self.anim_index = 0

    def update(self):
        self.acc = vec(0, 0)
        #keyboard input
        key = pg.key.get_pressed()
        if key[pg.K_a] and key[pg.K_d]:
            if self.direction == -1:
                self.acc.x += self.speed
            if self.direction == 1:
                self.acc.x += -self.speed
        elif key[pg.K_a]:
            self.move(-1)
        elif key[pg.K_d]:
            self.move(1)
        self.vel.x = (self.vel.x + self.acc.x) * self.friction
        if key[pg.K_w]:
            self.jump()

        #gravity
        self.acc.y = gravity(self.vel.y)
        self.vel.y += self.acc.y

        #rounding
        self.vel.y = round(self.vel.y, 4)
        self.vel.x = round(self.vel.x, 4)

        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        #colissions and moving
        collide_solid(self)

        self.animate()

    def move(self, direction):
        self.direction = direction
        self.acc.x += self.speed * direction

    def jump(self):
        if not self.stand:
            return

        self.vel.y = self.jumpheight

    def animate(self):
        self.anim_tick += 1
        if self.anim_tick == 10:

            if self.vel.x != 0:
                self.anim_index += 1
                if self.anim_index == len(self.images):
                    self.anim_index = 1
            else:
                self.anim_index = 0

            self.anim_tick = 0

            image = self.images[self.anim_index]
            if self.direction == 1:
                self.image = image
            elif self.direction == -1:
                self.image = pg.transform.flip(image, True, False)
