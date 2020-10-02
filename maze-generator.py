# pylint: disable=no-member

import sys
import time
import random
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
grid    = []
stack   = []
visited = []




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
            grid.append((x, y))
            x = x + w
        pygame.display.update()

def draw_current_cell(x, y) :
    pygame.draw.rect(window, COLOR_GREEN, (x + 1, y + 1, 18, 18), 0)
    pygame.display.update()

def draw_next_cell(x, y, w, direction) :
    # Go to the top cell
    if(direction == 'up') :
        pygame.draw.rect(window, COLOR_BLUE, (x + 1, y - w + 1, 19, 39), 0)
    # Go to the left cell
    elif(direction == 'left') :
        pygame.draw.rect(window, COLOR_BLUE, (x - w + 1, y + 1, 39, 19), 0)
    # Go to the bottom cell
    elif(direction == 'down') :
        pygame.draw.rect(window, COLOR_BLUE, (x + 1, y + 1, 19, 39), 0)
    # Go to the right cell
    elif(direction == 'right') :
        pygame.draw.rect(window, COLOR_BLUE, (x + 1, y + 1, 39, 19), 0)
    pygame.display.update()

def draw_backtracking_cell(x, y):
    pygame.draw.rect(window, COLOR_BLUE, (x + 1, y + 1, 18, 18), 0)
    pygame.display.update()

def create_maze_dfs(x, y, w) :
    draw_current_cell(x, y)
    stack.append((x, y))
    visited.append((x, y))

    while(len(stack) > 0) :
        # Check if neighbors are availablecls
        available_cells = []
        if( ((x, y - w) not in visited) and ((x, y - w) in grid) ) :
            available_cells.append('top')
        if( ((x - w, y) not in visited) and ((x - w, y) in grid) ) :
            available_cells.append('left')
        if( ((x, y + w) not in visited) and ((x, y + w) in grid) ) :
            available_cells.append('bottom')
        if( ((x + w, y) not in visited) and ((x + w, y) in grid) ) :
            available_cells.append('right')
        # Select a random neighbour
        if(len(available_cells) != 0) :
            next_cell = random.choice(available_cells)
            if(next_cell == 'top') :
                draw_next_cell(x, y, w, 'up')
                visited.append((x, y - w))
                stack.append((x, y - w))
                y = y - w
            elif(next_cell == 'left') :
                draw_next_cell(x, y, w, 'left')
                visited.append((x - w, y))
                stack.append((x - w, y))
                x = x - w
            elif(next_cell == 'bottom') :
                draw_next_cell(x, y, w, 'down')
                visited.append((x, y + w))
                stack.append((x, y + w))
                y = y + w
            elif(next_cell == 'right') :
                draw_next_cell(x, y, w, 'right')
                visited.append((x + w, y))
                stack.append((x + w, y))
                x = x + w
        else :
            x, y = stack.pop()
            draw_current_cell(x, y)
            draw_backtracking_cell(x, y)


draw_grid (0, 0, CELL_D, GRID_W, GRID_H)
create_maze_dfs(CELL_D, CELL_D, 20)

# Run the game loop
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()