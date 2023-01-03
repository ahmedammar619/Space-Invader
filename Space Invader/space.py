import pgzrun
from random import randint

HEIGHT = 600
WIDTH = 800
ship = Actor('ship')
ship.pos = (400,550)

lasers = []
stones = []


game_over = False
win_screen=False

score = 0
level = 1

speed = 0

boom = Actor('boom')
boom.pos = ship.pos




def draw():
    screen.blit('space',(0,0))
    ship.draw()

    # laser.draw()
    
    if game_over:
        screen.fill('black')
        display_message('Game Over','dumb')
        boom.draw()
    if win_screen:
        screen.fill('green')
        display_message('You Won','ra2e3')
        boom.draw()


    for laser in lasers:
        laser.draw()    

    for stone in stones:
        stone.draw()
    
    screen.draw.text('Score: ' + str(round(score, 2)), (330,10), color=(255,255,255), fontsize=30)
    screen.draw.text('Level: ' + str(round(level, 2)), (335,35), color=(255,255,255), fontsize=30)

        

def update():
    global game_over,score,speed,win_screen,level
    if keyboard.right and WIDTH>=ship.right and not game_over and not win_screen:
        ship.x = ship.x+10
    elif keyboard.left and ship.left>=0 and not game_over and not win_screen:
        ship.x = ship.x-10
 
    for stone in stones:
        stone.y += 3+speed
        if stone.colliderect(ship):
            game_over = True
        if stone.y >= 600 :  
            stones.remove(stone)
        for laser in lasers:
            if stone.colliderect(laser):
                stones.remove(stone)  
                lasers.remove(laser) 
                score+=10         
    
    for laser in lasers:
        laser.y-=10
        if laser.y <= 0:
            lasers.remove(laser)


    
    if randint(0,60) == 0:    #and not game_over
        stone = Actor('duck')
        stone.pos = (randint(20,(WIDTH-20)),-50)
        stones.append(stone)

    if score == 100:
        speed = 3
        level = 2
    elif score == 200:
        game_over = True
        win_screen =True
        level = 3

    if game_over:
        boom.pos = ship.pos


def on_key_down():
    if keyboard.space and not game_over and not win_screen: 
        laser = Actor('laser')
        laser.pos = ship.pos
        laser.y-=40
        lasers.append(laser)


def display_message(heading_text , sub_heading_text):
    screen.draw.text(heading_text, fontsize= 60, center = (WIDTH/2,HEIGHT/2), color = (255,255,255))
    screen.draw.text(sub_heading_text,
                     fontsize = 30,
                     center = (WIDTH/2, HEIGHT/2 +30),
                     color = (255,255,255))
   

        

pgzrun.go()

