import pygame as pg
from Globals import *

vec = pg.math.Vector2


class Hero(pg.sprite.Sprite):

    def __init__(self, x, y, spritesheet):
        pg.sprite.Sprite.__init__(self)
        self.images = slice_spritesheet(spritesheet, 10*4, 18*4 )
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        #self.rect = pg.Rect(0,0,30,17*4)
        self.rect.midbottom = (x,y)

        s_alive.add(self)
        s_player.add(self)
        s_all.add(self)

        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.direction = 1
        self.stand = False
        self.attack = False

        self.energy = 100
        self.damage = 50
        self.speed = 0.5
        self.jumpheight = -15
        self.friction = 0.6 #speed cap

        self.anim_tick = 0
        self.anim_index = 0
        self.anim_direction = 1

    def move(self, direction, oneInput=True):
        if oneInput:
            self.anim_direction = direction
        self.direction = direction
        self.acc.x = self.speed * self.direction
        self.acc.x += self.vel.x * self.friction
    def jump(self):
        if not self.stand:
            return

        self.vel.y = self.jumpheight

    def doAttack(self):
        att_range = 30
        sensor = pg.Rect(self.rect.center[0]+att_range*self.direction, self.rect.center[1]-5, 5, 10)
        for target in s_enemy:
            if sensor.colliderect(target.rect)==1:
                target.onHit(self.damage, self.direction)

    def onHit(self, dmg, direction):
        self.energy -= dmg

    #animations
    def Anim_Stand(self):
        self.anim_index = 0
        self.anim_tick = 0
        newImage(self)
    def Anim_Walk(self):
        if self.anim_tick < 10: #animation speed
            return
        self.anim_index += 1
        if self.anim_index == 7:
            self.anim_index = 1
        self.anim_tick = 0
        newImage(self)
    def Anim_Attack(self):
        if self.anim_tick < 10: #animation speed
            if self.anim_index>10:
                doAttack()
            return

        if self.anim_index < 8: #start animation
            self.anim_index = 8
        else:
            self.anim_index += 1
        if self.anim_index == 11:
            self.doAttack()
            self.attack = False
            self.anim_index = 0
            #self.attack = False
        if self.anim_index > 10:
            self.anim_index = 0
            self.attack = False
        self.anim_tick = 0

        newImage(self)

    def update(self):
        self.acc = vec(0,0)
        #keyboard input
        key = pg.key.get_pressed()
        if key[pg.K_LEFT] and key[pg.K_RIGHT]:
            if self.direction == -1:
                self.move(1, False)
            if self.direction == 1:
                self.move(-1, False)
        elif key[pg.K_LEFT]:
            self.move(-1)
        elif key[pg.K_RIGHT]:
            self.move(1)
        if key[pg.K_UP]:
            self.jump()
        if key[pg.K_q]:
            self.attack = True

        if self.attack:
            self.acc.x = 0

        self.vel.x = (self.vel.x + self.acc.x) * self.friction
        #gravity
        self.acc.y = gravity(self.vel.y)
        self.vel.y += self.acc.y #* self.friction


        if abs(self.vel.x) < 0.02:
            self.vel.x = 0
        #colissions and moving
        collide_solid(self)

        #animation:
        if self.attack:
            self.Anim_Attack()
        elif self.acc.x != 0:
            self.Anim_Walk()
        else:
            self.Anim_Stand()
        self.anim_tick+=1
