import pygame as pg
from pygame.draw import *
from pygame.transform import flip, rotozoom, rotate



def bg():
    bg_surface = pg.Surface((800, 1000), pg.SRCALPHA)
    mtn =  [(0, 595), (0, 342), (95, 107), (165, 272), (271, 146), (475, 451), (617, 140), (667, 193), (800, 41), (800, 665), (469, 666), (444, 657), (446, 599), (439, 596), (440, 577), (433, 566), (414, 562), (179, 562), (97, 575), (76, 571), (41, 578)]
    polygon(bg_surface, (179, 179, 179), mtn)
    polygon(bg_surface, (0, 0, 0), mtn, 1)

    grass = [(800, 665), (469, 666), (444, 657), (446, 599), (439, 596), (440, 577), (433, 566), (414, 562), (179, 562), (97, 575), (76, 571), (41, 578), (0, 592), (0, 1000), (800, 1000), (800, 665)]
    polygon(bg_surface, (170, 222, 135), grass)
    polygon(bg_surface, (0, 0, 0), grass, 1)
    return bg_surface


def leg():
    surf_leg = pg.Surface((35, 125), pg.SRCALPHA)
    ellipse(surf_leg, (255, 255, 255), (0, 0, 25, 55))
    ellipse(surf_leg, (255, 255, 255), (0, 55, 25, 55))
    ellipse(surf_leg, (255, 255, 255), (0, 109, 35, 16))
    return surf_leg


def lama():
    surf_lama = pg.Surface((200, 330), pg.SRCALPHA)
    ellipse(surf_lama, (255, 255, 255), (0, 140, 180, 80))
    surf_lama.blit(leg(), (10, 180))
    surf_lama.blit(leg(), (55, 200))
    surf_lama.blit(leg(), (95, 172))
    surf_lama.blit(leg(), (130, 200))
    ellipse(surf_lama, (255, 255, 255), (145, 35, 40, 130))
    ellipse(surf_lama, (255, 255, 255), (150, 12, 48, 30))
    circle(surf_lama, (229, 128, 255), (172, 24), 9)
    circle(surf_lama, (0, 0, 0), (175, 23), 4)
    polygon(surf_lama, (255, 255, 255), [(172, 18), (168, 17), (172, 18)], 4)
    polygon(surf_lama, (255, 255, 255), [(154, 22), (154, 28), (142,  7)])
    polygon(surf_lama, (255, 255, 255), [(161, 27), (164, 18), (152,  4)])
    return surf_lama


def flower():
    surf_flower = pg.Surface((80, 30), pg.SRCALPHA)
    petal = pg.Rect(0, 0, 32, 12)
    ellipse(surf_flower, (255, 255, 255), petal.move(10, 2))
    ellipse(surf_flower, (160, 160, 160), petal.move(10, 2), 1)
    ellipse(surf_flower, (255, 255, 255), petal.move(24, 0))
    ellipse(surf_flower, (160, 160, 160), petal.move(24, 0), 1)
    ellipse(surf_flower, (255, 255, 255), petal.move(37, 2))
    ellipse(surf_flower, (160, 160, 160), petal.move(37, 2), 1)
    ellipse(surf_flower, (255, 255, 0), petal.move(25, 10))
    ellipse(surf_flower, (255, 255, 255), petal.move(48, 10))
    ellipse(surf_flower, (160, 160, 160), petal.move(48, 10), 1)
    ellipse(surf_flower, (255, 255, 255), petal.move(40, 18))
    ellipse(surf_flower, (160, 160, 160), petal.move(40, 18), 1)
    ellipse(surf_flower, (255, 255, 255), petal.move(18, 17))
    ellipse(surf_flower, (160, 160, 160), petal.move(18, 17), 1)
    ellipse(surf_flower, (255, 255, 255), petal.move(2, 11))
    ellipse(surf_flower, (160, 160, 160), petal.move(2, 11), 1)
    return surf_flower


def meadow():
    surf_meadow = pg.Surface((300, 300), pg.SRCALPHA)
    circle(surf_meadow, (113, 200, 55), (150, 150), 150)
    surf_meadow.blit(flower(), (60, 170))
    surf_meadow.blit(rotate(flower(), 30), (60, 30))
    surf_meadow.blit(rotozoom(flower(), -20, 1.2), (170, 100))
    surf_meadow.blit(rotate(flower(), -15), (160, 40))
    surf_meadow.blit(rotate(flower(), -8), (190, 180))
    surf_meadow.blit(rotozoom(flower(), 8, 0.8), (30, 90))
    return surf_meadow


pg.init()
FPS = 30
screen = pg.display.set_mode((800, 1000))
screen.fill([175, 221, 233])


bg_surface = bg()
bg_surface.blit(rotozoom(meadow(), 0, 0.2), (0, 560))
bg_surface.blit(rotozoom(meadow(), 0, 0.2), (520, 660))
bg_surface.blit(rotozoom(meadow(), 0, 0.44), (531, 852))
bg_surface.blit(flip(rotozoom(meadow(), 0, 0.28), True, False), (693, 605))
bg_surface.blit(flip(rotozoom(meadow(), 0, 0.45), True, False), (693, 745))
bg_surface.blit(flip(rotozoom(meadow(), 0, 0.29), True, False), (730, 900))
bg_surface.blit(rotozoom(lama(), 0, 0.3), (310, 473))
bg_surface.blit(rotozoom(lama(), 0, 0.3), (220, 589))
bg_surface.blit(rotozoom(flip(lama(), True, False), 0, 0.3), (322, 655))
bg_surface.blit(rotozoom(flip(lama(), True, False), 0, 1.2), (668, 606))
bg_surface.blit(pg.transform.smoothscale(lama(), (500, 825)), (-300, 700))
#bg_surface.blit(rotozoom(lama(), 0, 2.5), (-300, 700))




screen.blit(bg_surface, (0, 0))

pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True


    if pg.mouse.get_pressed()[0]:
        print(pg.mouse.get_pos())
pg.quit()
