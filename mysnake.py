from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
ev=True
while ev==True:
    clock.tick(1)#limite la boule à 1image/sec

    for event in pg.event.get():
        if event.type == pg.KEYDOWN :
                if event.key == pg.K_q :
                    ev=False
        if event.type == pg.QUIT :
                ev=False

    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    screen.fill(random_color)
    pg.display.update()
    
pg.quit()
sys.exit()


