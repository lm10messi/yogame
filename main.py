
import random
import sys
import pygame
import math
from pygame import mixer
#initialization pygame
pygame.init()

#creating pygame windows

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Alien MIM Invasion")

# space ship / player creating
playerimg = pygame.image.load("ship.png")
playerx = 378
playery = 500
def player(x, y):
    screen.blit(playerimg, (x, y))
# display image
displayimg = pygame.image.load("space.jpg")



def screen_space():
    screen.blit(displayimg, (0,0))
#creat  enemy
enemyimg = [pygame.image.load("ufo.png"),pygame.image.load("cartoon.png"),pygame.image.load("death.png"),pygame.image.load("enemy2.png"),pygame.image.load("evil.png"),pygame.image.load("skull.png")]
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []






for i in range(6):
    enemyx.append(random.randint(0, 768))
    enemyy.append(random.randint(30, 60))
    enemyx_change.append(3)
    enemyy_change.append(0)

def enenmy(x, y, i):
    screen.blit(enemyimg[i], (x, y))

#creating bullet and bullet state can't see screen
bulletimg = pygame.image.load("bullet.png")
bulletx = 0

bullety = 500
bullety_change = 15

bullet_state ="ready"

def bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg,(x + 15, y))

#score
font = pygame.font.Font("crichd.otf", 32)
scrore_value = 0
def scroe_game(x, y):
    score = font.render("Score: " + str(scrore_value), True , (125, 125, 125))
    screen.blit(score, (x, y))
# game over

over_font = pygame.font.Font("crichd.otf", 62)

def game_over(x,y):
    finishgame = font.render("GAME OVER", True , (125, 125, 125))
    screen.blit(finishgame,(x,y))



def is_collision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt(math.pow(enemyx- bulletx, 2) + math.pow(enemyy- bullety , 2))
    if distance < 32:
        return True
    else:
        return False
# background music
mixer.music.load("background.wav")
mixer.music.play(-1)

while True:
    screen_space()

    #RGB
    #
    # screen.fill((125, 125, 125))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerx += 20
            if event.key == pygame.K_LEFT:
                playerx -= 20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if bullet_state is "ready":
                        bullet_sound = mixer.Sound("laser.wav")
                        bullet_sound.play()
                        bulletx = playerx
                        bullet(bulletx, bullety)
        if event.type == pygame.KEYUP:
            if event.key ==  pygame.K_RIGHT:
                playerx += 10
            if event.key == pygame.K_LEFT:
                playerx -= 10
    # movement of enemy
    for i in range(6):
        if enemyy[i] >= 460:
            for j in range(6):
                enemyy[j] = 2000
            game_over(360, 250)
            scroe_game(360, 270)
            break
        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0:
            enemyy[i] += 5
            enemyx_change[i] += float(.3)

        elif enemyx[i] >= 768:
            enemyy[i] += 5
            enemyx_change[i] -= float(.3)
        # when collide between enemy and bullet

        collision = is_collision(enemyx[i], enemyy[i], bulletx, bullety)
        if collision:
            collision_sound = mixer.Sound("explosion.wav")
            collision_sound.play()
            scrore_value += 1
            bullety = 500
            bullet_state = "ready"
            enemyx[i] = random.randint(0, 768)
            enemyy[i] = random.randint(30, 60)

        enenmy(enemyx[i], enemyy[i], i)
    #barrel window
    if playerx <= 0:
        playerx = 0
    if playerx >= 736:
        playerx = 736
    #bullet movement
    if bullet_state is "fire":
        bullet(bulletx, bullety)
        bullety -= bullety_change

    if bullety <= 0:
        bullety = 450
        bullet_state = "ready"

    player(playerx,playery)
    scroe_game(10 ,10)

    pygame.display.update()
