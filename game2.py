"""

  Upload basic image into the game_display
"""

import pygame


pygame.init()

display_width = 800
display_height = 600

game_display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Unicornio')

black = (0, 0, 0)
white = (255, 255, 255)
clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('image.png')


def unicron(x,y):
    game_display.blit(carImg, (x,y))

x =  (display_width * 0.45)
y = (display_height * 0.8)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    game_display.fill(black)
    unicron(x,y)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
