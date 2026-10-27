from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
ev=True
while ev==True:
    clock.tick(1)#limite la boule à 1image/sec

    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == pg.K_q :
                    ev=False
        if event.type == pg.QUIT :
                ev=False

    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    x, y = 100, 200            # coin supérieur gauche, en pixels
    width, height = 20, 20     # largeur et hauteur, en pixels
    color = (255, 0, 0)        # rouge, en (R, V, B)
    screen.fill([0,0,0]) #on remplit le fond de noir
    rect = pg.Rect(x, y, width, height)
    pg.draw.rect(screen, color, rect)
    pg.display.update()
    
pg.quit()
sys.exit()


def drawboard():
    screen.fill([0,0,0]) #on remplit le fond de noir
    x, y = 0,0           # coin supérieur gauche, en pixels
    width, height = 20, 20     # largeur et hauteur, en pixels
    color = (255, 255, 255)        # blanc, en (R, V, B)
    
    for k in range (15):
        x+=40
        y+=40
        rect = pg.Rect(x, y, width, height)
        pg.draw.rect(screen, color, rect)
        
    pg.display.update()

