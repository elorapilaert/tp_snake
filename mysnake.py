from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

SNAKE = [
   (10, 15),
   (11, 15),
   (12, 15),
]

DIRECTION =(1,0)

def draw_snake(snake):
      width, height = 20, 20
      color=(255,0,0) #couleur du serpent
      
      for k in snake: #dessin case par case
            rect = pg.Rect(k[0]*20, k[1]*20, width, height)
            pg.draw.rect(screen, color, rect)

def move_snake(snake, direction):
      snake.pop(0) #retire la queue
      snake.append((snake[-1][0]+direction[0], snake[-1][1]+direction[1])) #avance la tête

def drawboard():
    screen.fill([0,0,0]) #on remplit le fond de noir
    x, y = 0,0           # coin supérieur gauche, en pixels
    width, height = 20, 20     # largeur et hauteur, en pixels
    color = (255, 255, 255)        # blanc, en (R, V, B)
    
    for k in range (30):
        x=20*k
        for j in range (15):
            y=40*j +(k%2)*20 #on décale la première case si laligne est impaire
            rect = pg.Rect(x, y, width, height)
            pg.draw.rect(screen, color, rect)
        

ev=True
while ev==True:
    clock.tick(2)#limite la boule à 1image/sec

    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == pg.K_q :
                    ev=False
        if event.type == pg.QUIT :
                ev=False

    drawboard()
    draw_snake(SNAKE)
    pg.display.update()
    move_snake(SNAKE, DIRECTION)

    
pg.quit()
sys.exit()

#le serpent disparait lorqu'il atteint le bord de la fenêtre


