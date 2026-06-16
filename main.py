import random
import sys

import pygame as pg

pg.init()

WIDTH = 1152
HEIGHT = 648

screen = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)
clock = pg.time.Clock()

room = pg.image.load("assets/room.png").convert()

suspects = [
    pg.image.load("assets/suspects/blue.png").convert_alpha(),
    pg.image.load("assets/suspects/green.png").convert_alpha(),
    pg.image.load("assets/suspects/pink.png").convert_alpha(),
    pg.image.load("assets/suspects/orange.png").convert_alpha(),
    pg.image.load("assets/suspects/purple.png").convert_alpha(),
]

suspect = random.choice(suspects)

while True:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.blit(room, (0, 0))
    screen.blit(suspect, (0, 0))

    pg.display.flip()
