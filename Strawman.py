import pygame as pg
from Globals import *

vec = pg.math.Vector2

class Strawman(pg.sprite.Sprite):

    def __init__(self, x, y, spritesheet):
        pg.sprite.Sprite.__init__(self)
        self.images = slice_spritesheet(spritesheet, 14*4, 17*4)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x,y)

        s_alive.add(self)
        s_enemy.add(self)
        s_all.add(self)

        self.direction = 1
        self.stand = False
        self.vel = vec(0,0)
        self.hit =  False
        self.speed = 0

        self.energy = 9999999
        self.friction = 0.87

        self.anim_direction = 1
        self.anim_speed = 1
        self.anim_tick = 0
        self.anim_index = 0

    def onHit(self, dmg, direction):
        self.hit = True
        self.energy -= dmg
        self.anim_direction = -direction
        self.anim_speed = dmg


    def Anim_Rotate(self):
        if self.anim_tick < 400/self.anim_speed: #animation speed
            return
        self.anim_index += 1
        if self.anim_index == 8:
            self.anim_index = 0
            self.hit = False
        self.anim_tick = 0
        self.anim_speed -= 1
        newImage(self)

    def update(self):
        self.acc = vec(0,0)
        #gravity
        self.vel.y += gravity(self.vel.y)
        collide_solid(self)
        #animation
        if self.hit:
            self.Anim_Rotate()
        self.anim_tick += 1
