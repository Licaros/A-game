import pygame as pg

#settings
WIDTH = 800
HEIGHT = 600
pg.display.set_caption("A Game")
framerate = 60
scale = 20
#sprite Constants
PLAYER_FRICTION = 0.8



#sprite groups
s_player = pg.sprite.Group()
s_enemy  = pg.sprite.Group()
s_solid  = pg.sprite.Group()
s_trigger = pg.sprite.Group()
s_all    = pg.sprite.Group()
s_alive = pg.sprite.Group()


def gravity(vel):
    # deriv of 0.01*x² + 0.1*x
    return 0.025*abs(vel) + 0.1
