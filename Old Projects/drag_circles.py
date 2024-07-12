import pygame as p
p.init()
screen = p.display.set_mode([800, 600])
p.display.set_caption("click and draw to draw dots")
keep_going = True
mouseDown = False
WHITE = (255, 255, 255)
radius = 15
while keep_going:
    for event in p.event.get():
        if event.type == p.QUIT:
            keep_going = False
        if event.type == p.MOUSEBUTTONDOWN:
            mouseDown = True
            
        if event.type == p.MOUSEBUTTONUP:
            mouseDown = False
    if mouseDown:
        spot = p.mouse.get_pos()
        p.draw.circle(screen, WHITE, spot, radius)
    
    p.display.update()

p.quit()