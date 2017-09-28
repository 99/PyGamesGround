import pygame as pg

pg.init()

black = (0, 0, 0)
crashed = False
display = display_width, display_height = 800, 600
speed = [4, 4]

game_display = pg.display.set_mode(display)
pg.display.set_caption('Unicornio')
unicorn_img = pg.image.load("image.png")

clock = pg.time.Clock()


def unicron(x, y):
    game_display.blit(unicorn_img, display)

x =  (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0

while not crashed:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            crashed = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                x_change = - 5
            elif event.key == pg.K_RIGHT:
                x_change = 5
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                x_change = 0

    x += x_change

    game_display.fill(black)
    unicorn(x, y)

    pg.display.update()
    clock.tick(60)

pg.quit()
quit()
