# Start Stuff
import pygame as p
p.init()
DIS_WIDTH = 550
DIS_HEIGHT = 550
screen = p.display.set_mode([DIS_WIDTH, DIS_HEIGHT])
GAME = True
BACKGROUND = (50, 115, 168)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen.fill(BACKGROUND)
tileSize = 50
gridHeight = 500
gridWidth = 500
posx = 0
posy = 0
box = [0,0]
spot = None
mouseDown = False
sudokuBoard1 = [0,0,0,0,0,0,0,0,0]
sudokuBoard2 = [0,0,0,0,0,0,0,0,0]
sudokuBoard3 = [0,0,0,0,0,0,0,0,0]
sudokuBoard4 = [0,0,0,0,0,0,0,0,0]
sudokuBoard5 = [0,0,0,0,0,0,0,0,0]
sudokuBoard6 = [0,0,0,0,0,0,0,0,0]
sudokuBoard7 = [0,0,0,0,0,0,0,0,0]
sudokuBoard8 = [0,0,0,0,0,0,0,0,0]
sudokuBoard9 = [0,0,0,0,0,0,0,0,0]

    

# Main Loop
while GAME:
   
    # Grid
    for posy in range(tileSize, (DIS_HEIGHT - tileSize), tileSize):
        for posx in range(tileSize, (DIS_WIDTH - tileSize), tileSize):
            tile = p.Rect((posx, posy), (tileSize, tileSize))
            p.draw.rect(screen, WHITE, tile, 1)
            
        # Keys
    for event in p.event.get():
        print(box)
        print(spot)
        spot = p.mouse.get_pos()
        if event.type == p.QUIT:
            GAME = False
        elif event.type == p.MOUSEBUTTONDOWN:
            mouseDown = True
        elif event.type == p.MOUSEBUTTONUP:
            mouseDown = False
         # Click Detection (checks where you clicked)
        if spot[0] < (tileSize*2) and spot[0] > tileSize:
                box[0] = 1
        elif spot[0] < (tileSize*3) and spot[0] > (tileSize*2):
                box[0] = 2
        elif spot[0] < (tileSize*4) and spot[0] > (tileSize*3):
                box[0] = 3
        elif spot[0] < (tileSize*5) and spot[0] > (tileSize*4):
                box[0] = 4
        elif spot[0] < (tileSize*6) and spot[0] > (tileSize*5):
                box[0] = 5
        elif spot[0] < (tileSize*7) and spot[0] > (tileSize*6):
                box[0] = 6
        elif spot[0] < (tileSize*8) and spot[0] > (tileSize*7):
                box[0] = 7
        elif spot[0] < (tileSize*9) and spot[0] > (tileSize*8):
                box[0] = 8
        elif spot[0] < (tileSize*10) and spot[0] > (tileSize*9):
                box[0] = 9
                
        elif spot[1] < (tileSize*2) and spot[1] > tileSize:
                box[1] = 1
        elif spot[1] < (tileSize*3) and spot[1] > (tileSize*2):
                box[1] = 2
        elif spot[1] < (tileSize*4) and spot[1] > (tileSize*3):
                box[1] = 3
        elif spot[1] < (tileSize*5) and spot[1] > (tileSize*4):
                box[1] = 4
        elif spot[1] < (tileSize*6) and spot[1] > (tileSize*5):
                box[1] = 5
        elif spot[1] < (tileSize*7) and spot[1] > (tileSize*6):
                box[1] = 6
        elif spot[1] < (tileSize*8) and spot[1] > (tileSize*7):
                box[1] = 7
        elif spot[1] < (tileSize*9) and spot[1] > (tileSize*8):
                box[1] = 8
        elif spot[1] < (tileSize*10) and spot[1] > (tileSize*9):
                box[1] = 9
                
        if mouseDown:
               # if event.type == p.KEYDOWN:
                  #  if event.key == p.K_1:
            
            numrect = p.Rect((box[0]*50, box[1]*50), (tileSize, tileSize))
            p.draw.rect(screen, BLACK, numrect)
            
    p.display.update()

p.quit()
        