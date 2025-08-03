import pgzrun
import random

WIDTH = 1000
HEIGHT = 800

ship = Actor("ship")
enemys = []
bullets = []
score = 0
gameover = False
ship.pos = 500,750
win = False
speed = 2

for i in range(random.randint(1,7)):
    enemys.append(Actor("spaceship_bee"))
    enemys[i].x = random.randint(10,950) + 50
    enemys[i].y = 50


def draw ():
    screen.fill("Black")
    ship.draw()
    screen.draw.text("Score = "+ str(score), (10,10), color = ("White"))
    for i in enemys:
        i.draw()
    for i in bullets:
        i.draw()
    if gameover == True:
        screen.fill("Black")
        screen.draw.text("GAME OVER \n score = " + str(score), center = (500,300) ,fontsize = 60, color = "Red")
    #if win == True:
        #screen.fill ("Black")
        #screen.draw.text("You Won \n score = " + str(score), center = (500,300), fontsize = 60, color = "White")
    



def update():
    global score, gameover, win,speed
    for i in enemys:
        i.y = i.y + speed

    if keyboard.left and ship.x > 10:
        ship.x = ship.x - 5
    if keyboard.right and ship.x <950:
        ship.x  = ship.x + 5

    
    for bullet in bullets:
            bullet.y = bullet.y - 5
            for enemy in enemys:
                if bullet.colliderect(enemy):
                    score = score + 1
                    enemys.remove(enemy)
            
    for enemy in enemys:
        if enemy.y > 750:
            gameover = True             
    
    if len(enemys) == 0 :
        for i in range(random.randint(1,7)):
            enemys.append(Actor("spaceship_bee"))
            enemys[i].x = random.randint(10,950) + 50
            enemys[i].y = 50
            speed = speed + 0.2

    
            







def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y
        




pgzrun.go()


