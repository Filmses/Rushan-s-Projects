import pygame as p
import time
p.init()
DIS_WIDTH = 700
DIS_HEIGHT = 500
screen = p.display.set_mode([DIS_WIDTH, DIS_HEIGHT])
p.display.set_caption("PyPaint")
WHITE = (255, 255, 255)
screen.fill(WHITE)
keep_going = True
mouseDown = False
draw = True
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (122, 122, 122)
color = BLACK
shape = "circle"
size = 15
recWidth = int(DIS_WIDTH*0.1)
recHeight = int(DIS_HEIGHT*0.05)
redRectangle = p.Rect((3, 3), (recWidth, recHeight))
greenRectangle = p.Rect((recWidth + 3, 3), (recWidth, recHeight))
blueRectangle = p.Rect((recWidth * 2, 3), (recWidth, recHeight))
topRectangle = p.Rect((0, 0),(DIS_WIDTH, 2*recHeight))

def restore():
    p.draw.rect(screen, RED, redRectangle)
    p.draw.rect(screen, GREEN, greenRectangle)
    p.draw.rect(screen, BLUE, blueRectangle)
    
    
    
restore()
# Image buttons
buttonMinus = p.image.load("button_minus.png")
buttonPlus = p.image.load("button_plus.png")
buttonDelete = p.image.load("button_delete.png")

buttonMinus = p.transform.scale(buttonMinus, (recHeight, recHeight))
buttonPlus = p.transform.scale(buttonPlus, (recHeight, recHeight))
buttonDelete = p.transform.scale(buttonDelete, (recHeight, recHeight))

minusRect = buttonMinus.get_rect(topleft = (0, recHeight))
plusRect = buttonPlus.get_rect(topleft = (recHeight, recHeight))
deleteRect = buttonDelete.get_rect(topleft = (recHeight*2, recHeight))

while keep_going:
    for event in p.event.get():
        if event.type == p.QUIT:
            keep_going = False
        if event.type == p.MOUSEBUTTONDOWN:
            spot = p.mouse.get_pos()
            if minusRect.collidepoint(spot):
                size -= 5
                time.sleep(0.1)
            elif plusRect.collidepoint(spot) and size < recHeight - 5:
                size += 5
                time.sleep(0.1)
            elif deleteRect.collidepoint(spot) and size < recHeight - 5:
                screen.fill(WHITE)
                restore()
            else:
                mouseDown = True 
        if event.type == p.MOUSEBUTTONUP:
            mouseDown = False
            
    spot = p.mouse.get_pos()
    if mouseDown:
        if draw:
            p.draw.circle(screen, color, spot, size)
        if size <= 0:
            size = 5
        if redRectangle.collidepoint(spot):
            color = RED
        elif greenRectangle.collidepoint(spot):
            color = GREEN
        elif blueRectangle.collidepoint(spot):
            color = BLUE
    
    p.draw.rect(screen, GRAY, topRectangle)
    restore()
    screen.blit(buttonMinus, minusRect)
    screen.blit(buttonPlus, plusRect)
    screen.blit(buttonDelete, deleteRect)
    
    p.draw.circle(screen, color, (DIS_WIDTH - size, size), size)
    if spot[0] <= 250 and spot[1] < 75:
        draw = False
    else:
        draw = True
    
    p.display.update()
    

            
    
    

p.quit()