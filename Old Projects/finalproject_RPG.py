# Presets
import pygame as p
import time
p.init()
DIS_WIDTH = 1900
DIS_HEIGHT = 1000
screen = p.display.set_mode([DIS_WIDTH, DIS_HEIGHT])
GRASS_GREEN = (132, 241, 0)
BLACK = (0, 0, 0)
collide = None

# Classes
class Structure:
    def __init__(self, image, posX, posY, collision, type, scale1, scale2):
        self.image = image
        self.posX = posX
        self.posY = posY
        self.collision = collision
        self.type = type
        self.scale1 = scale1
        self.scale2 = scale2
        self.rect = self.image.get_rect()
        self.rect.x = self.posX
        self.rect.y = self.posY
        p.draw.rect(screen, (255, 255, 255), self.rect)
        
class BoxCollider:
    def __init__(self, x, y, w, h):
        self.w = w
        self.h = h
        self.rect = p.Rect([x, y], (w, h))
        self.rect.x = x
        self.rect.y = y
        self.top = self.rect.y
        self.bottom = self.rect.y + h
        self.left = self.rect.x
        self.right = self.rect.x + w
        
    def draw(self):
        p.draw.rect(screen, GRASS_GREEN, self.rect)
    
    def click(self):
        action = False
        spot = p.mouse.get_pos()
        if event.type == p.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(spot):
                action = True
                time.sleep(0.1)
        elif event.type == p.MOUSEBUTTONUP:
            action = False
        return action
        
class NPC:
    def __init__(self, image, posX, posY, rectX, rectY, npc):
        self.image = image
        self.posX = posX
        self.posY = posY
        self.npc = npc
        self.scale = DIS_WIDTH*0.09
        self.rect = self.image.get_rect()
        self.rect.x = rectX
        self.rect.y = rectY
        
    def dialogue(self, dialogue):
        myFont = p.font.SysFont("Courier", 30)
        text = myFont.render(str(dialogue), True, BLACK)
        text_rect = text.get_rect(topleft = (DIS_WIDTH / 3.2, DIS_HEIGHT / 7))
        screen.blit(text, text_rect)
        
class Player:
    def __init__(self, image):
        self.image = image
        self.x = 0
        self.y = 0
        self.scale = DIS_WIDTH*0.05
        self.rect = self.image.get_rect()
        self.rect.x = (DIS_WIDTH/2) - (self.scale/2)
        self.rect.y = (DIS_HEIGHT/2) - (self.scale/2)
        self.top = self.rect.y
        self.bottom = self.rect.y + self.image.get_height()
        self.left = self.rect.x
        self.right = self.rect.x + self.image.get_width()
        print(self.rect)
        
    def move(self, direction, structurelist, bclist):
        collide = None
        
        if direction == "up":
            for i in bclist:
                if self.rect.colliderect(i.rect):
                    if (self.top - i.bottom) <=5:
                        pass
                    else:
                        collide = "up"
            if not collide == "up":
                for i in structurelist:
                    i.posY += 5
                for i in bclist:
                    i.rect.y += 5
                player.y += 1
                player.image = p.image.load("player_up.png")
                player.image = p.transform.scale(player.image, (player.scale, player.scale))
                
        if direction == "down":
            for i in bclist:
                    if self.rect.colliderect(i.rect):
                        if (self.bottom - i.top) <=5:
                            pass
                        else:
                            collide = "down"
            if not collide == "down":
                for i in structurelist:
                    i.posY -= 5
                for i in bclist:
                   i.rect.y -= 5
                player.y -= 1
                player.image = p.image.load("player_down.png")
                player.image = p.transform.scale(player.image, (player.scale, player.scale))
                
        if direction == "left":
            for i in bclist:
                if self.rect.colliderect(i.rect):
                    if (self.right - i.left) <=5:
                        pass
                    else:
                        collide = "left"
            if not collide == "left":
                for i in structurelist:
                    i.posX += 5
                for i in bclist:
                   i.rect.x += 5
                player.x += 1
                player.image = p.image.load("player_left.png")
                player.image = p.transform.scale(player.image, (player.scale, player.scale))
        if direction == "right":
            for i in bclist:
                if self.rect.colliderect(i.rect):
                    if (self.left - i.right) <=5:
                        pass
                    else:
                        collide = "right"
            if not collide == "right":
                for i in structurelist:
                    i.posX -= 5
                for i in bclist:
                   i.rect.x -= 5
                player.x -= 1
                player.image = p.image.load("player.png")
                player.image = p.transform.scale(player.image, (player.scale, player.scale))

player = Player(p.image.load("player_down.png"))
player.image = p.transform.scale(player.image, (player.scale, player.scale))
player.rect = player.image.get_rect()
player.rect.x = (DIS_WIDTH/2) - (player.scale/2)
player.rect.y = (DIS_HEIGHT/2) - (player.scale/2)

npc_dialogue = p.image.load("npc_dialogue.png")
npc_dialogue = p.transform.scale(npc_dialogue, (DIS_WIDTH*0.8, DIS_HEIGHT*0.8))
        
# Structure Instances
Path = Structure((p.image.load("backdrop1.png")), DIS_WIDTH*0.285, DIS_HEIGHT*0.39, False, "other", DIS_WIDTH*0.4, DIS_HEIGHT*0.4)
Path.image = p.transform.scale(Path.image, (Path.scale1, Path.scale2))
Path.rect = Path.image.get_rect()

Lone_Shack = Structure((p.image.load("backdrop2.png")), DIS_WIDTH/3, -(DIS_HEIGHT/6), True, "other", DIS_WIDTH*0.3, DIS_WIDTH*0.3)
Lone_Shack.image = p.transform.scale(Lone_Shack.image, (Lone_Shack.scale1, Lone_Shack.scale2))
Lone_Shack.rect = Lone_Shack.image.get_rect()

Farm = Structure((p.image.load("backdrop3.png")), DIS_WIDTH*0.8, -(DIS_HEIGHT/6), False, "other", DIS_WIDTH*0.4, DIS_WIDTH*0.3)
Farm.image = p.transform.scale(Farm.image, (Farm.scale1, Farm.scale2))
Farm.rect = Farm.image.get_rect()

# NPC Instances
Lone_Farmer = NPC((p.image.load("lone_farmer.png")), DIS_WIDTH*0.6, DIS_HEIGHT*0.39, DIS_WIDTH*0.6, DIS_HEIGHT*0.39, "quest")
Lone_Farmer.image = p.transform.scale(Lone_Farmer.image, (Lone_Farmer.scale, Lone_Farmer.scale*0.8))
Lone_Farmer.rect = Lone_Farmer.image.get_rect()

# Colliders
Lone_ShackBC = BoxCollider(Lone_Shack.posX, Lone_Shack.posY, Lone_Shack.image.get_width(), Lone_Shack.image.get_height())
Farm1BC = BoxCollider(Farm.posX, Farm.posY, Farm.image.get_width(), (Farm.image.get_height()/5))
Farm2BC = BoxCollider((Farm.posX+725), Farm.posY, (Farm.image.get_width()/20), Farm.image.get_height())
Farm3BC = BoxCollider(Farm.posX, (Farm.posY+500), Farm.image.get_width(), (Farm.image.get_height()/8))
Lone_FarmerBC = BoxCollider(Lone_Farmer.posX, Lone_Farmer.posY, Lone_Farmer.image.get_width(), Lone_Farmer.image.get_height())

# Assets List
bc = [Lone_ShackBC, Farm1BC, Farm2BC, Farm3BC, Lone_FarmerBC]
spawnStuff = [Path, Lone_Shack, Farm, Lone_Farmer]
exitButton = p.Rect((DIS_WIDTH*0.86, DIS_HEIGHT*0.12), (DIS_WIDTH*0.025, DIS_WIDTH*0.025))
NPCDialogue = ["Hello Traveler!"]

# update() function    
def update():
    # Structure & NPC Stuff
    screen.fill(GRASS_GREEN)
    for i in bc:
        i.draw()
    for i in spawnStuff:
        screen.blit(i.image, (i.posX, i.posY))
    # Player Stuff
    screen.blit(player.image, ((DIS_WIDTH/2) - (player.scale/2), (DIS_HEIGHT/2) - (player.scale/2)))
    p.draw.rect(screen, (0, 0, 0), player.rect, 2)
    
update()

# Game Loop
inGame = True
while inGame:
    p.key.set_repeat(20,20)
    for event in p.event.get():
        if event.type == p.QUIT:
            inGame = False
        # Movement
        if event.type == p.KEYDOWN:
            if event.key == p.K_w:
                player.move("up", spawnStuff, bc)
                update()
            if event.key == p.K_a:
                player.move("left", spawnStuff, bc)
                update()
            if event.key == p.K_s:
                player.move("down", spawnStuff, bc)
                update()
            if event.key == p.K_d:
                player.move("right", spawnStuff, bc)
                update()
        # Clicking
        if Lone_FarmerBC.click():
            screen.blit(npc_dialogue, (DIS_WIDTH/10, DIS_HEIGHT/10))
            p.draw.rect(screen, BLACK, exitButton, 2)
            p.draw.line(screen, BLACK, (DIS_WIDTH*0.86, DIS_HEIGHT*0.12), (DIS_WIDTH*0.885, DIS_HEIGHT*0.165), 2)
            p.draw.line(screen, BLACK, (DIS_WIDTH*0.86, DIS_HEIGHT*0.165), (DIS_WIDTH*0.885, DIS_HEIGHT*0.12), 2)
            Lone_Farmer.dialogue(NPCDialogue[0])
        if event.type == p.MOUSEBUTTONDOWN:
            spot = p.mouse.get_pos()
            if exitButton.collidepoint(spot):
                update()
        p.display.update()
p.quit()