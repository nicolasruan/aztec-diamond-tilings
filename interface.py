import pygame, sys
import time
from pygame.locals import *

from partitions import *

# set up pygame
pygame.init()

# set up the window
disp = pygame.display.set_mode((640, 640), 0, 32)
pygame.display.set_caption('Aztec Diamond')

# set up the colors
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# set up fonts
font = pygame.font.SysFont(None, 48)

### set up the text
##text = basicFont.render('Hello world!', True, WHITE, BLUE)
##textRect = text.get_rect()
##textRect.centerx = windowSurface.get_rect().centerx
##textRect.centery = windowSurface.get_rect().centery
##
### draw the white background onto the surface
disp.fill(WHITE)


N = 50
S = 5


def draw_block(x, y, col):
    pygame.draw.rect(disp, col, ( (320 -N*S +S*x, 320-S*y), (S, S)))
    pygame.display.update()

def draw_horizontal(x, y, col):
    pygame.draw.rect(disp, col, ( (320 -N*S +S*x, 320-S*y), (2*S, S)))
    pygame.display.update()
    time.sleep(0.01)

def draw_vertical(x, y, col):
    pygame.draw.rect(disp, col, ( (320 -N*S +S*x, 320-S*y), (S, 2*S)))
    pygame.display.update()
    time.sleep(0.01)
    

l0 = Partition([])
l1 = Partition([2])
l2 = Partition([1])
l3 = Partition([1,1])
l4 = Partition([1])
l5 = Partition([1,1])
l6 = Partition([])

LL = random_partitions(N)

PC = configuration(LL)

x0 = 0
y0 = 0
x = 0
y = 0

for i in range(0, 2*N+1):
    K = 0
    if i % 2 == 0:
        K = N
        y0-=1
    else:
        K = N+1
        x0+=1
    for j in range(0, K):
        if PC[i][j] == 0:
            col = GRAY
        else:
            col = BLACK
        draw_block(x, y, col)
        x += 1
        y += 1
    x = x0
    y = y0

x0 = 0
y0 = 0
x = 0
y = 0

for i in range(0, 2*N+1):
    K = 0
    if i % 2 == 0:
        K = N
        y0-=1
    else:
        K = N+1
        x0+=1
    for j in range(0, K):
        if PC[i][j] == 0:
            if PC[i+1][j-(i%2)] == 0:
                col = BLUE
                draw_vertical(x, y, col)
                PC[i][j] = -1
                PC[i+1][j-(i%2)] = -1
            elif PC[i+1][j-(i%2)+1] == 0:
                col = GREEN
                draw_horizontal(x, y, col)
                PC[i][j] = -1
                PC[i+1][j-(i%2)+1] = -1
        elif PC[i][j] == 1:
            if j-i%2>=0 and PC[i+1][j-(i%2)] == 1:
                col = RED
                draw_vertical(x, y, col)
                PC[i][j] = -1
                PC[i+1][j-(i%2)] = -1
            elif PC[i+1][j-(i%2)+1] == 1:
                col = YELLOW
                draw_horizontal(x, y, col)
                PC[i][j] = -1
                PC[i+1][j-(i%2)+1] = -1
        x += 1
        y += 1
    x = x0
    y = y0


##
### draw a green polygon onto the surface
##pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
##
### draw some blue lines onto the surface
##pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
##pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
##pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)
##
### draw a blue circle onto the surface
##pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)
##
### draw a red ellipse onto the surface
##pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)
##
### draw the text's background rectangle onto the surface
##pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))
##
### get a pixel array of the surface
##pixArray = pygame.PixelArray(windowSurface)
##pixArray[480][380] = BLACK
##del pixArray
##
### draw the text onto the surface
##windowSurface.blit(text, textRect)

# draw the window onto the screen
pygame.display.update()

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
