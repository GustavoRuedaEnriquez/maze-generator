# pylint: disable=no-member

import sys
import time
import pygame


if( len(sys.argv) == 1 ) :
    print('Invalid syntax, please type the command correctly.') 
    print('Usage:') 
    print('\tpython maze-generator.py [WIDTH] [HEIGHT]')
    print('\tWIDTH  - The number of cells alongside the width. The valid values are [5 - 30]')
    print('\tHEIGHT - The number of cells alongside the height. The valid values are [5 - 30]')
    print()
    print('Example:')
    print('\tpython maze-generator.py 25 20')
    print()
    exit()

if( (int(sys.argv[1]) < 5 or int(sys.argv[1]) > 30) or (int(sys.argv[2]) < 5 or int(sys.argv[2]) > 30) ) :
    print('Invalid dimensions, please enter valid ones.') 
    print('Usage:') 
    print('\tpython maze-generator.py [WIDTH] [HEIGHT]')
    print('\tWIDTH  - The number of cells alongside the width. The valid values are [5 - 30]')
    print('\tHEIGHT - The number of cells alongside the height. The valid values are [5 - 30]')
    print()
    print('Example:')
    print('\tpython maze-generator.py 25 20')
    print()
    exit()

# GRID WIDTH, HEIGHT AND CELL DIMENSIONS (WIDTH AND HEIGHT)
GRID_W = int(sys.argv[1])
GRID_H = int(sys.argv[2])
CELL_D = 20

# GUI WINDOW DIMENSIONS
SCREEN_W = 650
SCREEN_H = 650

# COLORS DEFINITIONS
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED   = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE  = (0, 0, 255)

# FRAMES
FPS = 30

# CELLS ARRAY
unvisited_cells = []
visited_cells   = []



# set up pygame
pygame.init()
pygame.mixer.init()
# set up the window
window = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption('Maze generator')
clock = pygame.time.Clock()


def draw_grid (x, y, w, rows, columns) :
    for i in range(0, columns):
        x = w
        y = y + w
        for j in range(0, rows):
            # Top cell margin
            pygame.draw.line(window, COLOR_WHITE, [x, y], [x + w, y])
            # Left cell margin
            pygame.draw.line(window, COLOR_WHITE, [x, y], [x, y + w])
            # Bottom cell margin
            pygame.draw.line(window, COLOR_WHITE, [x, y + w], [x + w, y + w])
            # Right cell margin
            pygame.draw.line(window, COLOR_WHITE, [x + w, y], [x + w, y + w])
            x = x + w
        pygame.display.update()


def create_maze_dfs() :
    print('TODO')



draw_grid (0, 0, CELL_D, GRID_W, GRID_H)
create_maze_dfs()

# run the game loop
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()