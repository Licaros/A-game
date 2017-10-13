from Globals import *
import pygame as pg

vec = pg.math.Vector2

class Knight(pg.sprite.Sprite):

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
        self.direction = -1
        self.stand = False
        self.wall = False
        self.attack = False
        self.target = 0

        self.energy = 100
        self.damage = 20
        self.speed = 0.3
        self.jumpheight = -10
        self.friction = 0.6

        self.anim_tick = 0
        self.anim_index = 0
        self.anim_direction = -1

    def move(self, direction):
        self.direction = direction
        self.anim_direction = direction
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
        self.vel.x += 10*direction
        self.vel.y += -5

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
        pass

    def update(self):
        if self.energy<=0:
            self.kill()
        self.acc = vec(0,0)
        self.x = self.rect.midbottom[0]
        self.y = self.rect.midbottom[1]
        #walking
        #self.sensor = pg.Rect(self.x + (self.rect.width+8)/2*self.direction, self.y, -1, 1)
        if self.target == 0:
            for i in s_player:
                if distance(self, i) < 400:
                    self.target = i
                    break
        elif distance(self, self.target) > 500:
            self.target = 0
        if self.target != 0:
            if self.target.rect.x < self.rect.x:
                self.move(-1)
            else:
                self.move(1)
        if self.wall:
            self.jump()
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



#old

#        if self.target == 0:
#            for i in s_player:
#                if distance(self, i) < 400:
#                    self.target = i
#                    break
#        elif distance(self, self.target) > 500:
#            self.target = 0
#        if self.target != 0:
#            if self.target.rect.x < self.rect.x:
#                self.move(-1)
#            else:
#                self.move(1)
