"""
Bouncing Unicornio

"""

import pygame as pg

pg.init()

black = (0, 0, 0)
crashed = False
display = display_width, display_height = 800, 600
speed = [4, 4]

game_display = pg.display.set_mode(display)
pg.display.set_caption('Unicornio')
unicorn = pg.image.load("image.png")

unicornio = unicorn.get_rect()

while not crashed:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            crashed = True

    unicornio = unicornio.move(speed)
    if unicornio.left < 0 or unicornio.right > display_width:
        speed[0] = -speed[0]
    if unicornio.top < 0 or unicornio.bottom > display_height:
        speed[1] = - speed[1]

    game_display.fill(black)
    game_display.blit(unicorn, unicornio)
    pg.display.flip()

pg.quit()
quit()


