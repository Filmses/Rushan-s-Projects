#Main File
#Infinite Run 2D Side-scroll

import pygame
import lesson6_Entities as Entities
from random import randint

pygame.init()
screen = pygame.display.set_mode([Entities.DIS_WIDTH,Entities.DIS_HEIGHT])
clock = pygame.time.Clock()
count = 0

RED = (255,0,0)
BLUE = (0,255,0)
SKY = (135,206,235)
GREEN = (0,0,255)
BROWN = (139,69,19)
keep_going = True
fall = True
# Main Game Loop Stuff
pc = Entities.Player(30, screen, [100,Entities.FLOOR])
ground = pygame.Rect((0,630), (Entities.DIS_WIDTH, 90))
proj = None

# main loop
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pc.loc[1] == Entities.FLOOR:
                    pc.move(5)
                    fall = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            proj = pc.attack()

    screen.fill(SKY) # blank the screen to draw a new frame
    pygame.draw.rect(screen, BROWN, ground) 
    
    #Spawn random enemy or obstacle
    if count == 50:  ##This is not seconds!
        rand = randint(0,1)
        if rand == 0:
            Entities.Enemy(30, screen, [Entities.SPAWN_X, Entities.FLOOR])
        else:
            Entities.Obstacle(30, screen, [Entities.SPAWN_X, Entities.FLOOR])
        count = 0
     
    ##Jump
    if pc.loc[1] < Entities.FLOOR and not fall:
        pc.move(5)
        if pc.loc[1] <= 480:
            fall = True
    #Gravity
    if pc.loc[1] >= 480 and pc.loc[1] < Entities.FLOOR and fall:
        pc.move(-5)

    #Check for collisions
    pc.update()
    if proj != None:
        proj = proj.update()
        if proj != None:
            proj = proj.checkCollision()
    for enemy in Entities.enemiesSpawned:
        enemy.move(-10)
        enemy.update()
        keep_going = enemy.checkCollision(pc)
        if not keep_going:
            break
    
    
    if keep_going:
        for obs in Entities.obstaclesSpawned:
            obs.move()
            obs.update()
            keep_going = obs.checkCollision(pc)
            if not keep_going:
                break
    
    count+=1
    
    pygame.display.update()
    clock.tick(30) # game loop repeats at 120 frames per second
    #pygame.time.delay(8) # alternative to using clock

pygame.quit()            