import json
import pygame as pg#importy pygame as pg
import random as r #importy random as r
import math#importy mat
import time#importy time
import sys #importy sys

pg.init()#clcok
clock = pg.time.Clock() # clock time 

#----------------------importing the settings-----------------------------
def load_settings():#how you load settings
  try:#trying to load the settings
    with open("data/settings.json", "r") as f:#opening the settings.json
      return json.load(f)#reterning the json
  except (FileNotFoundError, json.JSONDecodeError):#validation incase of an error
    return {"music": True, "resolution": [1152, 648]} # we need to put settings here, deez be defaults ok !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def save_settings(settings):#saving the changed settings
  with open("data/settings.json", "w") as f:#opening the settigs 
    json.dump(settings, f)#dumping the json
    
settings = load_settings()


resolution = settings["resolution"]#settings resolution
screen_width, screen_height = resolution#resolution 

screen = pg.display.set_mode((screen_width, screen_height), pg.RESIZABLE) # resizeable screen 
#--------------vertual screen display-------------------------
running = True
VIRTUAL_WIDTH = screen_width
VIRTUAL_HEIGHT = screen_height
virtual_surface = pg.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT), pg.SRCALPHA)

pg.display.set_caption("Untitled Interrogation Game") #game title

# colours
black = (0, 0, 0)#this is the colour pink
white = (255, 255, 255)#this is the colour orange
green = (110, 194, 100)#this is the colour of hakari
gamblergreen = (109,237,83)#this is the second colour of hakari 
blue = (101, 110, 195)#this is the colour of blue judas
bluejudas = (134, 206, 203)#this is the oher colour of blue judas
red = (195, 101, 110)#this is the colour of red judas
redjudas = (255,0,69)#this is the other colour of red judas
yellow = (181, 195, 101)#this is the colour of miwa 
specialgradeyellow = (213, 157, 36)#this is the colour of miwa in modulo

#------------------------------------import assets-------------------------------------

def load_sprite(img, filetype):
  sprite = pg.image.load("data/" + img + "." + filetype).convert_alpha()
  return sprite

pastel_pink = (255, 182, 193)
pastel_blue = (174, 198, 207)
pastel_yellow = (253, 253, 150)
pastel_purple = (203, 153, 201)
pastel_green = (119, 221, 119)

try:
    bg_interrogation = load_sprite("bg_interrogation", "png")
    desk_foreground = load_sprite("desk_foreground", "png")
    character_body = load_sprite("char_body_transparent", "png")
    face_sad = load_sprite("face_sad", "png")
    face_angry = load_sprite("face_angry", "png")
except:
    bg_interrogation = pg.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT), pg.SRCALPHA)
    bg_interrogation.fill(pastel_pink)
    desk_foreground = pg.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT), pg.SRCALPHA)
    pg.draw.rect(desk_foreground, pastel_blue, (0, 400, VIRTUAL_WIDTH, 248))
    character_body = pg.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT), pg.SRCALPHA)
    face_sad = pg.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT), pg.SRCALPHA)
    face_angry = pg.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT), pg.SRCALPHA)

current_scene = "interrogation"
orb_x = 400
orb_speed = 3
current_char_color = pastel_purple
current_face = face_sad

while running:
    virtual_surface.fill(pastel_pink) 
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()
            
        if event.type == pg.VIDEORESIZE:
            screen_width, screen_height = event.size
            screen = pg.display.set_mode((screen_width, screen_height), pg.RESIZABLE)
            
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_c:
                current_scene = "computer"
            if event.key == pg.K_i:
                current_scene = "interrogation"

    if current_scene == "interrogation":
        orb_x += orb_speed
        if orb_x > 700 or orb_x < 450:
            orb_speed *= -1
            
        if orb_x > 600:
            current_char_color = pastel_purple
            current_face = face_angry
        else:
            current_char_color = pastel_green
            current_face = face_sad
            
    elif current_scene == "computer":
        pass

    if current_scene == "interrogation":
        virtual_surface.blit(bg_interrogation, (0, 0))
        pg.draw.circle(virtual_surface, current_char_color, (orb_x, 220), 100)
        virtual_surface.blit(character_body, (0, 0))
        virtual_surface.blit(current_face, (0, 0))
        virtual_surface.blit(desk_foreground, (0, 0))
        
    elif current_scene == "computer":
        virtual_surface.fill(pastel_yellow)
        font = pg.font.SysFont(None, 48)
        text = font.render("computah time... press I to go back", True, gamblergreen)
        virtual_surface.blit(text, (250, 300))

    scaled_surface = pg.transform.scale(virtual_surface, (screen_width, screen_height))
    screen.blit(scaled_surface, (0, 0))
    
    pg.display.flip()
    clock.tick(60)
