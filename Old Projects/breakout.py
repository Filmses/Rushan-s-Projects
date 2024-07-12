import pygame
import random
pygame.init()

DIS_WIDTH = 1280
DIS_HEIGHT = 720

screen = pygame.display.set_mode([DIS_WIDTH, DIS_HEIGHT])
clock = pygame.time.Clock()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Ball:
    def __init__(self, size, color):
        self.color = color
        self.size = size
        self.score = 0
        self.pos = [DIS_WIDTH / 2, DIS_HEIGHT / 2]
        self.speed = [2, 2]
        
        self.rect = pygame.rect.Rect(self.pos, (size, size))
        self.opp_aim = -50
    def move(self):
        self.bounce_edge()
        
        self.rect.move_ip(self.speed)
        self.pos = self.rect[0:2]
        
        pygame.draw.rect(screen, self.color, self.rect)
    
    def bounce_edge(self):
        if self.pos[1] + self.size > DIS_HEIGHT or self.pos[1] < 0:
            self.speed[1] *= -1
        if self.pos[0] < 0 or self.pos[0] + self.size > DIS_WIDTH:
            self.speed[0] *= -1
    def bounce_bumper(self, bumper):
        if self.rect.colliderect(bumper):
            self.speed[0] *= -1
            return True
        return False
    
        bumper_aim = self.opp_aim
    def set_aim(self):
        self.opp_aim = random.randint(-120, 45)
class Bumper():
    def __init__(self, position, color, dimensions):
        self.color = color
        self.dim = dimensions
        
        self.pos = position
        self.rect = pygame.rect.Rect(self.pos, self.dim)
        self.aim = -50
    def follow_mouse(self):
        self.pos[1] = pygame.mouse.get_pos()[1]
        offset = -1 * (self.rect[1] - self.pos[1])
        
        if self.pos[1] > DIS_HEIGHT - self.dim[1]:
            self.rect.update((self.pos[0], DIS_HEIGHT - self.dim[1]), self.dim)
        else:
            self.rect.move_ip(0, offset)
        
        pygame.draw.rect(screen, self.color, self.rect)
    
    def follow_ball(self, ball):
        self.pos[1] = ball.pos[1] + self.aim
        offset = -1 * (self.rect[1] - self.pos[1])
        
        if self.pos[1] > DIS_HEIGHT - self.dim[1]:
            self.rect.update((self.pos[0], DIS_HEIGHT - self.dim[1]), self.dim)
        elif self.pos[1] < 0:
            self.rect.update((self.pos[0], 0), self.dim)
        else:
            self.rect.move_ip(0, offset)
            
        pygame.draw.rect(screen, self.color, self.rect)
        

# Main Game Loop Stuff
my_font = pygame.font.SysFont("Comic Sans", 48)
my_ball = Ball(25, GREEN)
left_bumper = Bumper([80, 0], RED, [25, 100])
# Bricks
bricks = []
x_scale = DIS_WIDTH // 10
y_scale = DIS_HEIGHT // 5
x_offset = DIS_WIDTH / 2
color = BLUE
for x in range(5):
    for y in range(5):
        bricks.append(Bumper((x*x_scale + x_offset, y*y_scale), color, (25, 100)))
    if x > 1 and x < 3:
        color = GREEN
keep_going = True
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    screen.fill((0, 0, 0))
    text = my_font.render(str(my_ball.score), True, (255, 255, 255))
    text_rect = text.get_rect(center = (DIS_WIDTH / 4, DIS_HEIGHT / 4))
    screen.blit(text, text_rect)
    left_bumper.follow_mouse()
    
    
    my_ball.move()
    my_ball.bounce_bumper(left_bumper)
    
    for brick in bricks:
        pygame.draw.rect(screen, brick.color, brick.rect)
        if my_ball.bounce_bumper(brick):
            bricks.remove(brick)
            my_ball.score += 1
        
    pygame.display.update()
    clock.tick(120)

pygame.quit()
            
pygame.quit()