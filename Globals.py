import pygame as pg
pg.init()
pg.font.init
#settings
WIDTH = 1366
HEIGHT = 768
pg.display.set_caption("A Game")
framerate = 70
scale = 20
font = pg.font.SysFont("Arial", 15)
timer = 0
timerstart = False
airfriction = 0.8
#sprite groups
boxes = []
s_player  = pg.sprite.Group()
s_enemy   = pg.sprite.Group()
s_solid   = pg.sprite.Group()
s_trigger = pg.sprite.Group()
s_all     = pg.sprite.Group()
s_alive   = pg.sprite.Group()

def slice_spritesheet(sheet, w, h):
    images = []
    master = pg.image.load(sheet).convert_alpha()
    masterw, masterh = master.get_size()

    for i in range(int(masterw / w)):
        images.append(master.subsurface((i*w, 0, w, h)))

    return images

def gravity(vel):
    # deriv of 0.01*x² + 0.1*x
    return (0.05*abs(vel) + 0.3 )* airfriction

def newImage(subj): #for animation
    image = subj.images[subj.anim_index]
    if subj.anim_direction == 1:
        subj.image = image
    elif subj.anim_direction == -1:
        subj.image = pg.transform.flip(image, True, False)
    subj.anim_tick = 0

def collide_solid(subj):
    subj.stand = False

    subj.vel.y = round(subj.vel.y, 4)
    subj.vel.x = round(subj.vel.x, 4)
    subj.rect.x += subj.vel.x + 0.5* subj.friction
    touch = pg.sprite.spritecollide(subj, s_solid, False)
    subj.wall=False
    if touch:
        subj.wall=True
        if subj.vel.x > 0:
            subj.rect.right = touch[0].rect.left
        elif subj.vel.x < 0:
            subj.rect.left = touch[0].rect.right
        subj.vel.x = 0
    subj.rect.y += subj.vel.y
    touch = pg.sprite.spritecollide(subj, s_solid, False)
    if touch:
        if subj.vel.y > 0:
            subj.rect.bottom = touch[0].rect.top
            subj.stand = True
        elif subj.vel.y < 0:
            subj.rect.top = touch[0].rect.bottom
        subj.vel.y = 0
def distance(a, b):
    return abs(a.rect.x - b.rect.x)
