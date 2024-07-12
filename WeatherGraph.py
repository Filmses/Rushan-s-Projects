# starting stuff :P
import pygame as p
p.init()
disWidth = 1000
disHeight = disWidth*0.6
screen = p.display.set_mode([disWidth, disHeight])
start = True
data = [0, 1, 2, 3, 4]

# colors
BACKGROUND = (50, 115, 168)
BLACK = (0, 0, 0)
RED = (239, 49, 17)
screen.fill(BACKGROUND)

# graph variables
minHeight = disHeight*0.92
maxHeight = disHeight*0.08
minWidth = disWidth*0.06
maxWidth = disWidth*0.94
space = maxWidth/(len(data)-1)
units = minHeight/max(data)

# main loop
while start:
    for event in p.event.get():
        p.draw.line(screen, BLACK, (0, minHeight), (disWidth, minHeight), 10)
        p.draw.line(screen, BLACK, (minWidth, 0), (minWidth, disHeight), 10)

        for count, num in enumerate(data):
            if count == len(data)-1:
                pass
            elif count == 0:
                p.draw.line(screen, RED, (((space*count + (minWidth*1.1))), minHeight-(num*units)), (space*(count+1), minHeight-(data[count+1]*units)), 10)
            else:
                p.draw.line(screen, RED, (((space*count)), minHeight-(num*units)), (space*(count+1), minHeight-(data[count+1]*units)), 10)
                

        # quit function
        if event.type == p.QUIT:
            start = False
        p.display.update()


p.quit()
