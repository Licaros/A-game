import pygame as pg
from Globals import *

vec = pg.math.Vector2

class StandartEnemy(pg.sprite.Sprite):

    def __init__(self, x, y, spritesheet):
        pg.sprite.Sprite.__init__(self)
        self.images = slice_spritesheet(spritesheet, 10*4, 18*4)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x,y)

        s_alive.add(self)
        s_enemy.add(self)
        s_all.add(self)

        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.direction = 1
        self.stand = False
        self.attack = False

        self.energy = 100
        self.damage = 20
        self.speed = 0.6
        self.jumpheight = -20
        self.friction = 0.6

        self.anim_tick = 0
        self.anim_index = 0
        self.anim_direction = 1

    #def getTarget(self, targetarray):
    #    self.targets = targetarray


    def move(self, direction):
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
        for target in s_player:
            if sensor.colliderect(target.rect)==1:
                target.onHit(self.damage, self.direction)
        #screen.blit(sensor)
        self.anim_tick = 100

    def onHit(self, dmg, direction):
        self.energy -= dmg

    def Anim_Stand(self):
        self.anim_index = 0
        self.anim_tick = 0
        newImage(self)
    def Anim_Walk(self):
        pass
    def Anim_Attack(self):
        pass

    def update(self):
        self.acc = vec(0,0)

        self.vel.x = (self.vel.x + self.acc.x) * self.friction
        #gravity
        self.acc.y = gravity(self.vel.y)
        self.vel.y += self.acc.y

        if abs(self.vel.x) < 0.02:
            self.vel.x = 0

        collide_solid(self)

        if self.attack:
            self.Anim_Attack()
        elif self.acc.x != 0:
            self.Anim_Walk()
        else:
            self.Anim_Stand()
        self.anim_tick+=1
