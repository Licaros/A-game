import pygame as pg


class Ground(pg.sprite.Sprite):

    def __init__(self, image, s_group):
        #pg.sprite.Sprite.__init__(self, s_group)
        super(Ground, self).__init__()
        self.x = 0
        self.y = 580
        self.image = pg.image.load(image).convert_alpha()
        self.rect = pg.Rect((self.x,self.y),(-10,800))
        s_group.add(self)

    def show(self, screen):
        screen.blit(self.image,(self.x,self.y))
