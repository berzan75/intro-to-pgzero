import pgzrun
from random import randint

#vari to make a gamescreen
WIDTH= 400
HEIGHT= 400
TITLE="BERNA"

def draw():
    width=WIDTH
    height=HEIGHT -200

    for i in range(20):

        r=randint(120,201)
        g=randint(123,255)
        b=100

        rect=Rect((0,0),(width, height))
        rect.center=(200,200)
        screen.draw.rect(rect,(r, g, b))


        height+=10
        width-= 10


pgzrun.go()
