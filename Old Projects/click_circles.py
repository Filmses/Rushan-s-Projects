import pygame as p
p.init()
screen = p.display.set_mode([800, 600])
p.display.set_caption("click to place dots")
keep_going = True
RED = (255, 0, 0)
radius = 25
while keep_going:
    for event in p.event.get():
        if event.type == p.QUIT:
            keep_going = False
        if event.type == p.MOUSEBUTTONDOWN:
            spot = event.pos
            p.draw.circle(screen, RED, spot, radius)
    p.display.update()

p.quit()
        