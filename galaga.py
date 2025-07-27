import pgzrun
import random

WIDTH = 1000
HEIGHT = 600

ship = Actor("ship")
enemys = []
bullets = []
score = 0
gameover = False
ship.pos = 500,550

for i in range(random.randint(1,7)):
    enemys.append(Actor("spaceship_bee"))
    enemys[i].x = random.randint(10,950) + 50
    enemys[i].y = 50


def draw ():
    screen.fill("Black")
    ship.draw()
    for i in enemys:
        i.draw()
    for i in bullets:
        i.draw()



def update():
    for i in enemys:
        i.y = i.y + random.randint(1,3)

    if keyboard.left and ship.x > 10:
        ship.x = ship.x - 2
    if keyboard.right and ship.x <950:
        ship.x  = ship.x + 2

def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y





pgzrun.go()


