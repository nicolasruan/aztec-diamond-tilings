import pygame, sys
import time
from pygame.locals import *
from partitions import *


# SETTINGS

N = 50 # order of aztec diamond

weights = [1/2 for k in range(0, int(N*(N+1)/2))] #list of N*(N+1)/2 weights in [0, 1]

SCREEN_X = 640

SCREEN_Y = 640

animate = True


# graphics
pygame.init()

disp = pygame.display.set_mode((SCREEN_X, SCREEN_Y), 0, 32)
pygame.display.set_caption('Aztec Diamond')

# colors
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
disp.fill(WHITE)

S = min( int(SCREEN_X/(2*N+1)), int(SCREEN_Y/(2*N+1)))


def draw_block(x, y, col, size):
    pygame.draw.rect(disp, col, ( (int(SCREEN_X/2) -N*size +size*x, int(SCREEN_Y/2)-size*(y+1)), (size, size)))
    if animate:
        pygame.display.update()

def draw_horizontal(x, y, col, size):
    pygame.draw.rect(disp, col, ( (int(SCREEN_X/2) -N*size +size*x, int(SCREEN_Y/2)-size*(y+1)), (2*size, size)))
    if animate:
        pygame.display.update()

def draw_vertical(x, y, col, size):
    pygame.draw.rect(disp, col, ( (int(SCREEN_X/2) -N*size +size*x, int(SCREEN_Y/2)-size*(y+1)), (size, 2*size)))
    if animate:
        pygame.display.update()



def main():
    LL = random_partitions(N, weights)
    PC = configuration(LL)


    # draw particle configuration
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
            draw_block(x, y, col, S)
            x += 1
            y += 1
        x = x0
        y = y0

    # draw domino tiling
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
                    draw_vertical(x, y, col, S)
                    PC[i][j] = -1
                    PC[i+1][j-(i%2)] = -1
                elif PC[i+1][j-(i%2)+1] == 0:
                    col = GREEN
                    draw_horizontal(x, y, col, S)
                    PC[i][j] = -1
                    PC[i+1][j-(i%2)+1] = -1
            elif PC[i][j] == 1:
                if j-i%2>=0 and PC[i+1][j-(i%2)] == 1:
                    col = RED
                    draw_vertical(x, y, col, S)
                    PC[i][j] = -1
                    PC[i+1][j-(i%2)] = -1
                elif PC[i+1][j-(i%2)+1] == 1:
                    col = YELLOW
                    draw_horizontal(x, y, col, S)
                    PC[i][j] = -1
                    PC[i+1][j-(i%2)+1] = -1
            x += 1
            y += 1
        x = x0
        y = y0

main()


pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
