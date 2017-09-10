import pygame as pg
pg.init()
pg.font.init
#settings
WIDTH = 1366
HEIGHT = 768
pg.display.set_caption("A Game")
framerate = 60
scale = 20
font = pg.font.SysFont("Arial", 15)
timer = 0
timerstart = False
#sprite groups
s_player = pg.sprite.Group()
s_enemy  = pg.sprite.Group()
s_solid  = pg.sprite.Group()
s_trigger = pg.sprite.Group()
s_all    = pg.sprite.Group()
s_alive = pg.sprite.Group()

def slice_spritesheet(sheet, w, h):
    images = []
    master = pg.image.load(sheet).convert_alpha()
    masterw, masterh = master.get_size()

    for i in range(int(masterw / w)):
        images.append(master.subsurface((i*w, 0, w, h)))

    return images

def gravity(vel):
    # deriv of 0.01*x² + 0.1*x
    return 0.025*abs(vel) + 0.1

def newImage(subj): #for animation
    image = subj.images[subj.anim_index]
    if subj.anim_direction == 1:
        subj.image = image
    elif subj.anim_direction == -1:
        subj.image = pg.transform.flip(image, True, False)
    subj.anim_tick = 0

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
