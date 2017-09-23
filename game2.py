"""
 Display images with PyGame
"""

import pygame

pygame.init()
display_w = 800
display_h = 600

game_display = pygame.display.set_mode((display_w, display_h))
pygame.display.set_caption("GameGround")

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False 

img = pygame.image.load("Image.png")

def img(x,y):
    game_display.blot(img, (x,y))

x = (display_w *0.45)
