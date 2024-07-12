import pygame
pygame.init()
screen = pygame.display.set_mode([800, 600])
keep_going = True
RED = (255, 0, 0) # needs RGB value in a constant variable
radius = 500
while keep_going:
    for event in pygame.event.get(): # checks for events
        if event.type == pygame.QUIT: # checks if user closed out of the window
            keep_going = False
    pygame.draw.square(screen, RED, (100, 100), radius) 
    pygame.display.update() # updates the screen VERY IMPORTANT(PUT PARATHESES AT THE END ITS A FUNCTION)
pygame.quit()