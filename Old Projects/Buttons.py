import pygame as p
import time as t
p.init()
DIS_WIDTH = 550
DIS_HEIGHT = 550
screen = p.display.set_mode([DIS_WIDTH, DIS_HEIGHT])
BG = (66, 200, 245)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
tile_size = 50
keep_going = True
spot = None
mouseDown = False

class Game():
    def __init__(self, data):
        self.tile_list = []
        row_count = 0
        
       
        for row in data:
                col_count = 0
                for tile in row:
        
                    if tile == 1:
                        tile_rect = p.Rect(((col_count*tile_size),(row_count*tile_size) ), (tile_size, tile_size))
                        tile_rect.x = col_count*tile_size
                        tile_rect.y = row_count*tile_size
                        tile = tile_rect
                        self.tile_list.append(("DEFAULT", tile))
                    col_count += 1
                row_count += 1
            
    def draw(self):
        for tile in self.tile_list:
            if tile[0] == "SELECTED":
                p.draw.rect(screen, BLACK, tile[1])
            else:
                p.draw.rect(screen, WHITE, tile[1])
                
            
            
data = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

game = Game(data)

while keep_going:
    screen.fill(BG)
    spot = p.mouse.get_pos()
    game.draw()
    
    for event in p.event.get():
        if event.type == p.MOUSEBUTTONDOWN:
            mouseDown = True
        elif event.type == p.MOUSEBUTTONUP:
            mouseDown = False
        if mouseDown:
            count = 0
            for tile in game.tile_list:
                if tile[1].collidepoint(spot):
                    game.tile_list.remove(tile)
                    game.tile_list.insert(count, ("SELECTED", tile))
                    
    
        
        if event.type == p.QUIT: 
            keep_going = False
            
    p.display.update() 
p.quit()