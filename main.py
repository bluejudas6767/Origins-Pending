import random
import sys

import pygame as pg

pg.init()

WIDTH = 1152
HEIGHT = 648

screen = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)
clock = pg.time.Clock()

room = pg.image.load("assets/room.png").convert()

colour = (random.randint(50,200),random.randint(50,200),random.randint(50,200)) # generates an rgb colour, but limited between 50 and 200 to not make colours too dark/bright
suspect = pg.image.load("assets/white.png") # loads the suspect sprite
suspectColour = pg.Surface(suspect.get_size()).convert_alpha() 
suspectColour.fill(colour) # recolours the blank white sprite to the randomly generated colour
suspect.blit(suspectColour, (0,0), special_flags = pg.BLEND_RGBA_MULT) # idk what it does but the colour doesnt work without this line

scene = "interrogation"
x3, y3, w3, h3, x4, y4, w4, h4 = 1, 1, 1, 1, 1, 1, 1, 1 # placeholder since these do not yet exist
scenes = {
    "interrogation": {
        "notes": pg.Rect(305, 354, 604, 558),
        "suspect": pg.Rect(424, 106, 776, 278),
        "item": pg.Rect(x3, y3, w3, h3)
    },
    "computer": {
        "computer": pg.Rect(x4, y4, w4, h4)
    }
}

def interact(obj):
    global scene

    if scene == "interrogation":
        if obj == "notes":
            print("u clicked notes")
        elif obj == "suspect":
            print("u clicked suspect")
        elif obj == "item":
            print("u clicked item")
    elif scene == "computer":
        if obj == "computer":
            print("u clicked computer")

while True:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            print(event.pos)

            for obj, rect in scenes[scene].items():
                if rect.collidepoint(event.pos):
                    interact(obj)
                    break


    screen.blit(room, (0, 0))
    screen.blit(suspect, (0, 0))

    pg.display.flip()
