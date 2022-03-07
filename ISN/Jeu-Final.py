import pygame
pygame.init()
import random
import math
import time
from time import sleep, time
from pygame import mixer

#fond d'ecran
window = pygame.display.set_mode((900,900))
pygame.display.set_caption("First Game")
background = pygame.image.load('sol.png')

#effet sonores

#http://www.wavsource.com/sfx/sfx.htm (site pour effets sonores)

mixer.music.load("musique_jeu.wav")
mixer.music.play(5)
pygame.mixer.music.set_volume(0.05)

#projectile
epee = pygame.image.load('projectile.png')
epeeX = 0
epeeY = 350

# Enemy: class 1-
enemyImg1 = []
enemyX1 = []
enemyY1 = []
enemyX_change1 = []
enemyY_change1 = []
num_of_enemies1 = 4

for i in range(num_of_enemies1):
    enemyImg1.append(pygame.image.load('monster1.png'))
    enemyX1.append(random.randint(20, 800))
    enemyY1.append(random.randint(20, 700))
    enemyX_change1.append(random.choice([-6, -5, -4, 4, 5, 6]))
    enemyY_change1.append(50)
    
def enemy1(x, y, i):
    window.blit(enemyImg1[i], (x, y))

#Enemy: class 2-
enemyImg2 = []
enemyX2 = []
enemyY2 = []
enemyX_change2 = []
enemyY_change2 = []
num_of_enemies2 = 4

for i in range(num_of_enemies2):
    enemyImg2.append(pygame.image.load('monster2.png'))
    enemyX2.append(random.randint(20, 800))
    enemyY2.append(random.randint(20, 700))
    enemyY_change2.append(random.choice([-4, -3, -2, -1, 1, 2, 3, 4]))
    enemyX_change2.append(50)
    
def enemy2(x, y, i):
    window.blit(enemyImg2[i], (x, y))

#collision entre projectile et ennemi numero 2
def isCollision1_projectile(enemyX1, enemyY1, projectileX, projectileY):
    distance = math.sqrt(math.pow((enemyX1-30) - (projectileX-25), 2) + (math.pow((enemyY1-30) - projectileY, 2)))
    if distance < 27:
        return True
    else:
        return False

#collision entre projectile et ennemi numero 2
def isCollision2_projectile(enemyX2, enemyY2, projectileX, projectileY):
    distance = math.sqrt(math.pow((enemyX2-30) - (projectileX-25), 2) + (math.pow((enemyY2-30) - projectileY, 2)))
    if distance < 27:
        return True
    else:
        return False

#collision entre ennemi numero 1 et notre personnage
def isCollision1_ennemi(enemyX1, enemyY1, playerX, playerY):
    distance = math.sqrt(math.pow((enemyX1-30) - (playerX-32), 2) + (math.pow((enemyY1-30) - (playerY-32), 2)))
    if distance < 32:
        return True
    else:
        return False    


#collision entre ennemi numero 2 et notre personnage
def isCollision2_ennemi(enemyX2, enemyY2, playerX, playerY):
    distance = math.sqrt(math.pow((enemyX2-30) - (playerX-32), 2) + (math.pow((enemyY2-30) - (playerY-33), 2)))
    if distance < 32:
        return True
    else:
        return False    


# Score

score_value = 0
type_texte = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    window.blit(score, (x, y))

#game over
game_over_texte = pygame.font.Font('freesansbold.ttf', 50)    
overX = 125
overY = 400
    
def game_over(x,y):
    fin_jeu =  game_over_texte.render("GAME OVER: you scored " +str(score_value), True, (255, 255, 255))
    window.blit(fin_jeu, (x, y))
    
    
# vie du personnage
vie = 3
font = pygame.font.Font('freesansbold.ttf', 25)
vieX = 650
vieY = 10

def ecran_vie(x, y):
    vie_perso = font.render("Vies restantes: " +str(vie), True, (255, 255, 255))
    window.blit(vie_perso, (x, y))

def exit_game(x, y):
    leave = font.render("Press 'e' to exit the game", True, (255, 255, 255))
    remerciements = font.render("Merci d'avoir joué! Musique réalisée par Paul Nauche", True, (255,255,255))
    window.blit(remerciements, (x-170, y+230))
    window.blit(leave, (x, y+200))

#notre personnage
walkRight = pygame.image.load('perso_right.png')
walkLeft = pygame.image.load('perso_left.png')
walkUp = pygame.image.load('perso_avant.png')
walkDown = pygame.image.load('perso_arriere.png')
bouge_pas = pygame.image.load('perso_stop.png')
tir_epee = pygame.image.load('perso_sword.png')

playerX = 375
playerY = 350
width = 1
height = 1
vel = 10

clock = pygame.time.Clock()

left = False
right = False
up = False
down = False
  
  
#projectile
projectileImg = pygame.image.load('projectile.png')
projectileX = playerX
projectileY = playerY 
projectileX_change = 20
projectileY_change = 30
etat_projectile = "pret"

def tirer_projectile(x, y):
    global etat_projectile
    etat_projectile = "feu"
    window.blit(projectileImg, (x + 10, y + 10))


run = True
while run:
    clock.tick(100)
    
    window.blit(background, (0,0))  
    
    if left:  
        window.blit(walkLeft, (playerX, playerY))
                                 
    elif right:
        window.blit(walkRight, (playerX, playerY))
        
    elif up:  
        window.blit(walkUp, (playerX, playerY))
                                 
    elif down:
        window.blit(walkDown, (playerX, playerY))    
        
    else:
        window.blit(bouge_pas, (playerX, playerY))
        
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
       
    if keys[pygame.K_SPACE]:
                if etat_projectile is "pret":
                    BulletSound = mixer.Sound("son-proj.wav")
                    BulletSound.play()
                    projectileX = playerX
                    tirer_projectile(projectileX, projectileY)
    
    if keys[pygame.K_LEFT] and playerX > 120 - vel: 
        playerX -= vel
        left = True
        right = False
        down = False
        up = False
        
        
    elif keys[pygame.K_RIGHT] and playerX < 735 - vel:  
        playerX += vel
        left = False
        right = True
        down = False
        up =  False

    
    elif keys[pygame.K_UP] and playerY > 110 - vel: 
        playerY -= vel
        left = False
        right = False
        down = False
        up = True
        

    elif keys[pygame.K_DOWN] and playerY < 700 - vel:  
        playerY += vel
        left = False
        right = False
        down = True
        up = False
    
    else:
        window.blit(bouge_pas, (playerX, playerY))
        left = False
        right = False
        down = False
        up = False
     
     # Enemy class1 Movement:
    for i in range(num_of_enemies1):

        enemyX1[i] += enemyX_change1[i]
        if enemyX1[i] <= 120:
            enemyX_change1[i] = 4
            enemyY1[i] += enemyY_change1[i]
        elif enemyX1[i] >= 735:
            enemyX_change1[i] = -4
            enemyY1[i] += enemyY_change1[i]
        elif enemyY1[i] >= 700:
            enemyY_change1[i] = -50
            enemyY1[i] += enemyY_change1[i]
        elif enemyY1[i] <= 110:
            enemyY_change1[i] = 50
            enemyY1[i] += enemyY_change1[i]
    
    # Enemy class2 Movement:
    for i in range(num_of_enemies2):

        enemyY2[i] += enemyY_change2[i]
        if enemyY2[i] <= 120:
            enemyY_change2[i] = 4
            enemyX2[i] += enemyX_change2[i]
        elif enemyY2[i] >= 700:
            enemyY_change2[i] = -4
            enemyX2[i] += enemyX_change2[i]
        elif enemyX2[i] >= 700:
            enemyX_change2[i] = -50
            enemyX2[i] += enemyX_change2[i]
        elif enemyX2[i] <= 110:
            enemyX_change2[i] = 50
            enemyX2[i] += enemyX_change2[i]
    
    # Collision 1 entre projectile et ennemi
        collision1 = isCollision1_projectile(enemyX1[i], enemyY1[i], projectileX, projectileY)
        if collision1:
            Soncollision1 = mixer.Sound("monstre-contact.wav")
            Soncollision1.play()
            score_value += 1
            etat_projectile = "pret"
            projectileX = playerX
            projectileY = playerY
            enemyX1[i] = random.randint(0, 750)
            enemyY1[i] = random.randint(0, 750)
            enemyX_change1[i] = random.choice([-6, -5, -4, 4, 5, 6])
                

    # Collision 2 entre projectile et ennemi
        collision2 = isCollision2_projectile(enemyX2[i], enemyY2[i], projectileX, projectileY)
        if collision2:
            Soncollision1 = mixer.Sound("monstre-contact.wav")
            Soncollision1.play()
            score_value += 1
            etat_projectile = "pret"
            projectileX = playerX
            projectileY = playerY
            enemyX2[i] = random.randint(0, 750)
            enemyY2[i] = random.randint(0, 750)
            enemyY_change2[i] = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])

            
    # Collision 1 entre ennemi et personnage
        collision1_ennemi = isCollision1_ennemi(enemyX1[i], enemyY1[i], playerX, playerY)
        if collision1_ennemi:
            vie -= 1
            enemyX1[i] = random.randint(0, 750)
            enemyY1[i] = random.randint(0, 750)
            enemyX_change1[i] = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
            
     # Collision 2 entre ennemi et personnage
        collision2_ennemi = isCollision2_ennemi(enemyX2[i], enemyY2[i], playerX, playerY)
        if collision2_ennemi:
            vie -= 1
            enemyX2[i] = random.randint(0, 750)
            enemyY2[i] = random.randint(0, 750)
            enemyX_change2[i] = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])


        enemy1(enemyX1[i], enemyY1[i], i)
        enemy2(enemyX2[i], enemyY2[i], i)
    
   # mouvement projectile
    
    if projectileY <= 0:
        projectileY = playerY
        etat_projectile = "pret"

    if etat_projectile is "feu":
        window.blit(tir_epee, (playerX, playerY))
        tirer_projectile(projectileX, projectileY)
        projectileY -= projectileY_change
   
    if vie <= 0:
        game_over(overX, overY)
        exit_game(300, 450)
        vie = 0
        playerX = -1000
        playerY = -1000
        pygame.mixer.music.stop()
        gameover1 = pygame.mixer.Sound("game-over-music.wav")
        gameover1.set_volume(0.02)
        gameover1.play()
        if keys[pygame.K_e]:
            quit()
        
    

    ecran_vie(vieX, vieY)
    show_score(textX, textY)
    pygame.display.update() 


time.sleep(0.5)
pygame.quit()
time.sleep(10)
quit()