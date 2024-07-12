import pygame
pygame.init()
screen = pygame.display.set_mode([800, 600])
keep_going = True
COLOR = (colorVar1, colorVar2, colorVar3)# needs RGB value in a constant variable
colorVar1 = 0
colorVar2 = 0
colorVar3 = 0 
BLACK = (0, 0, 0)
width = 50
height = 50
radius = 50
posx = 100
posy = 100
speedx = .1
speedy = .1
while keep_going:
    for event in pygame.event.get(): # checks for events
        if event.type == pygame.QUIT: # checks if user closed out of the window
            keep_going = False
    screen.fill(BLACK)
    posx += speedx
    posy += speedy
    if posx <= 0 or posx + width >= 800:
        speedx = -speedx
        colorVar1 += 1
        colorVar2 += 1
        colorVar3 += 1
    if posy <= 0 or posy + height >= 600:
        speedy = -speedy
        colorVar1 += 1
        colorVar2 += 1
        colorVar3 += 1
    rectangle = pygame.Rect((posx, posy), (width, height))
    pygame.draw.rect(screen, COLOR, rectangle)
    pygame.display.update() # updates the screen VERY IMPORTANT(PUT PARATHESES AT THE END ITS A FUNCTION)
pygame.quit()