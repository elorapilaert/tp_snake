from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

def drawboard():
    screen.fill([0,0,0]) #on remplit le fond de noir
    x, y = 0,0           # coin supérieur gauche, en pixels
    width, height = 20, 20     # largeur et hauteur, en pixels
    color = (255, 255, 255)        # blanc, en (R, V, B)
    
    for k in range (30):
        x=20*k
        for j in range (15):
            y=40*j +(k%2)*20
            rect = pg.Rect(x, y, width, height)
            pg.draw.rect(screen, color, rect)
        

ev=True
while ev==True:
    clock.tick(1)#limite la boule à 1image/sec

    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == pg.K_q :
                    ev=False
        if event.type == pg.QUIT :
                ev=False

    drawboard()
    pg.display.update()
    
pg.quit()
sys.exit()



