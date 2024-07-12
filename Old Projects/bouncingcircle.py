import pygame
pygame.init()
screen = pygame.display.set_mode([800, 600])
keep_going = True
WHITE = (255, 255, 255)# needs RGB value in a constant variable
BLACK = (0, 0, 0)
radius = 50
posx = 100
posy = 100
speedx = 0.1
speedy = 0.1
while keep_going:
    for event in pygame.event.get(): # checks for events
        if event.type == pygame.QUIT: # checks if user closed out of the window
            keep_going = False
    screen.fill(BLACK)
    posx += speedx
    posy += speedy
    if posx - radius <= 0 or posx + radius >= 800:
        speedx = -speedx
    if posy - radius <= 0 or posy + radius >= 600:
        speedy = -speedy
    pygame.draw.circle(screen, WHITE, (posx, posy), radius) 
    pygame.display.update() # updates the screen VERY IMPORTANT(PUT PARATHESES AT THE END ITS A FUNCTION)
pygame.quit()