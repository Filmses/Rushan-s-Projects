import pygame
import random
import time

keep_going = True
WHITE = (255, 255, 255)
MAX_CIRCLE_SIZE = 100
MIN_CIRCLE_SIZE = 10
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
NUM_OF_CIRCLES = 100
SPEED = 1
MIN_RECTANGLE_HEIGHT_DIFFERENCE = -100
MAX_RECTANGLE_HEIGHT_DIFFERENCE = 100
RECTANGLE_HEIGHT = random.randint(MIN_RECTANGLE_HEIGHT_DIFFERENCE, MAX_RECTANGLE_HEIGHT_DIFFERENCE)
pygame.init()
screen = pygame.display.set_mode([DISPLAY_WIDTH, DISPLAY_HEIGHT])

# colors, locations, sizes arrays for 100 random dots
colors = []
locations = []
sizes = []

# store random values in colors, locations, sizes
for n in range(NUM_OF_CIRCLES):
    colors.append((random.randint(0, 255), random.randint(0, 255),
                   random.randint(0, 255)))
    locations.append((random.randint(0 - MAX_CIRCLE_SIZE, DISPLAY_WIDTH + MAX_CIRCLE_SIZE),
                      random.randint(0 - MAX_CIRCLE_SIZE, DISPLAY_HEIGHT + MAX_CIRCLE_SIZE)))
    sizes.append(random.randint(MIN_CIRCLE_SIZE, MAX_CIRCLE_SIZE))
    

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

    for n in range(NUM_OF_CIRCLES):
        pygame.draw.circle(screen, colors[n], locations[n], sizes[n])
        posx = locations[n][0] + SPEED
        posy = locations[n][1] + SPEED
        rectangle = pygame.Rect((posx, posy), (sizes[n], sizes[n] + RECTANGLE_HEIGHT))
        pygame.draw.rect(screen, colors[n - 1], rectangle)
        if posx > DISPLAY_WIDTH + MAX_CIRCLE_SIZE:
            posx -= DISPLAY_WIDTH + MAX_CIRCLE_SIZE * 2
        if posy > DISPLAY_HEIGHT + MAX_CIRCLE_SIZE:
            posy -= DISPLAY_HEIGHT + MAX_CIRCLE_SIZE * 2
        locations[n] = (posx, posy)

    pygame.display.update()
    screen.fill(WHITE)
    time.sleep(0.02)

pygame.quit()
