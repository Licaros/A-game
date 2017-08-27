import pygame as pg


class Hero(pg.sprite.Sprite):

    def __init__(self, image, s_group):
        self.x = 10
        self.y = 300
        self.xvel = 0
        self.yvel = 0
        self.xvelmax = 10
        self.xvelmin = -10
        self.direction = 0
        self.jump = True

        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        s_group.add(self)


    def move(self):
        #input
        #!! -Feature: hält man Right gedrückt und dann Left+Right gedrückt wird der
        #!!           neue Input (Left) akeptiert (man dreht sich)
        #!!           erlaubt schnelle Rektionen (Keine "Blockade")
        key = pg.key.get_pressed()
        speed = 1
        if key[pg.K_a] and key[pg.K_d]:
            if self.direction == -1:
                self.xvel += speed
            if self.direction == 1:
                self.xvel += -speed
        elif key[pg.K_a]:
            self.direction = -1
            self.xvel += -speed
        elif key[pg.K_d]:
            self.direction = 1
            self.xvel += speed
        else:
            self.direction = 0
        if key[pg.K_w] and not self.jump:
            self.jump = True
            self.yvel = -20

        self.yvel += 1

        #ground
        if (self.y+self.yvel) > 500:
            while self.y+self.yvel >500:
                self.yvel += -1
                self.jump = False

        #!! -Feature: Funktion für die Beschleunigung
        #friction on X Axcis
        if not key[pg.K_a] and not key[pg.K_d] and self.yvel == 0:
            #!! möglicherweise eine Funktion einbauen, damit das Movement
            #!! natürlicher wird
            if self.xvel > 0:
                self.xvel -= 1
            elif self.xvel < 0:
                self.xvel += 1

        #speedcap
        if self.xvel > self.xvelmax:
            self.xvel=self.xvelmax
        elif self.xvel < self.xvelmin:
            self.xvel=self.xvelmin
        #assign new position
        self.x += self.xvel
        self.y += self.yvel

    def colission(self, ground):
        while pg.sprite.collide_rect(self, ground):
            self.y += -1
            self.yvel = 0
            self.jump = False

    def show(self, screen):
        screen.blit(self.image,(self.x,self.y))
