# pylint: disable=no-member
# pylint: disable=unused-variable

"""
------------------------
| Maze-Generator       |
| Drawing utilities    |
------------------------
Author: Gustavo Adolfo Rueda Enríquez
Python 3.8

"""

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
os.environ['SDL_VIDEO_CENTERED'] = "True"

import random
import pygame

# WALL CONSTANT
WALL_CONST = 0

# SLOT CONSTANT
SLOT_CONST = 1

#X Y ORIGIN
ORIGIN = (0, 0)

#BISECT DIRECTIONS
VERTICAL, HORIZONTAL = 0,1

# GUI WINDOW DIMENSIONS
SCREEN_W = 800
SCREEN_H = 800

# CELL WIDTH (SQUARE CELLS)
CELL_W = 11

# FRAMES
FPS = 30

# COORDINATES OF THE FIRST SLOT
X_0 = 2 * CELL_W
Y_0 = 2 * CELL_W

# COLORS DEFINITIONS
COLOR_BLACK  = (0, 0, 0)
COLOR_GRAY   = (104, 104, 104)
COLOR_WHITE  = (255, 255, 255)
COLOR_RED    = (255, 0, 0)
COLOR_GREEN  = (0, 255, 0)
COLOR_BLUE   = (0, 0, 255)
COLOR_VIOLET = (153, 51, 153)

def init_screen(Title) :
    pygame.init()
    pygame.mixer.init()
    window = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption(Title)
    clock = pygame.time.Clock()
    return window, clock

def run_game_loop(Clock) :
    while True:
        Clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

def draw_maze(Window, maze_matrix):
  x = ORIGIN[0]
  y = ORIGIN[1]

  y = 2 * CELL_W
  for i in range(0, len(maze_matrix)):
    x = 2 * CELL_W
    for j in range(0, len(maze_matrix[i])):
      cell = pygame.Rect([x, y], [CELL_W, CELL_W])
      if maze_matrix[i][j] is WALL_CONST:
        pygame.draw.rect(Window, COLOR_VIOLET, cell)
      elif maze_matrix[i][j] is SLOT_CONST:
        pygame.draw.rect(Window, COLOR_WHITE, cell)
      x += CELL_W
    y += CELL_W
  pygame.display.update()


def draw_grid (Window, Rows, Columns) :
    grid = []
    x = ORIGIN[0]
    y = ORIGIN[1]

    # Draw a rectangle that will act as border of the whole maze
    x = CELL_W * 1.5
    y = CELL_W * 1.5
    total_width = CELL_W + (2 * Columns - 1) * CELL_W
    total_height = CELL_W + (2 * Rows - 1) * CELL_W
    wall = pygame.Rect([x, y], [total_width, total_height])
    pygame.draw.rect(Window, COLOR_GRAY, wall)

    for row in range(0, Rows) :
      x = 2 * CELL_W
      y = 2 * CELL_W if row == 0 else y + (2 * CELL_W)

      for col in range (0, Columns):
        # Draw usable slot.
        cell = pygame.Rect([x, y], [CELL_W, CELL_W])
        pygame.draw.rect(Window, COLOR_WHITE, cell)

        # Draw wall to the right, only draw it if not on the last column.
        wall_right = False
        if col < Columns - 1:
          wall = pygame.Rect([x + CELL_W, y], [CELL_W, CELL_W])
          pygame.draw.rect(Window, COLOR_GRAY, wall)
          wall_right = True

        # Update the value of x
        x += CELL_W
        if wall_right :
          x += CELL_W

      x = 2 * CELL_W

      # Draw a wall line at the bottom, only draw it if not on the last row
      if row < Rows - 1:
        wall = pygame.Rect([x, y + CELL_W], [(2 * Rows - 1) * CELL_W, CELL_W])
        pygame.draw.rect(Window, COLOR_GRAY, wall)
      pygame.display.update()
    return grid

def draw_grid_outer_line (Window, Rows, Columns) :
    grid = []
    start_x = ORIGIN[0] + CELL_W
    start_y = ORIGIN[1] + CELL_W
    end_x = start_x + (CELL_W * Rows)
    end_y = start_y + (CELL_W * Columns)
    # Top line margin
    pygame.draw.line(Window, COLOR_RED, [start_x, start_y], [end_x, start_y])
    # Left line margin
    pygame.draw.line(Window, COLOR_RED, [start_x, start_y], [start_x, end_y])
    # Bottom line margin
    pygame.draw.line(Window, COLOR_RED, [start_x, end_y], [end_x, end_y])
    # Right line margin
    pygame.draw.line(Window, COLOR_RED, [end_x, start_y], [end_x, end_y])
    pygame.display.update()
    return grid

def draw_bisect_grid (Window, Sx, Sy, Ex, Ey, Direction, Bx, By) :
    # Parse the grid coordinates to the display coordinates.
    parsed_sx = CELL_W * (Sx + 1)
    parsed_sy = CELL_W * (Sy + 1)
    parsed_ex = CELL_W * (Ex + 1)
    parsed_ey = CELL_W * (Ey + 1)
    parsed_bx = CELL_W * (Bx + 1)
    parsed_by = CELL_W * (By + 1)
    if Direction == HORIZONTAL :
        pygame.draw.line(Window, COLOR_WHITE, [parsed_sx, parsed_by], [parsed_ex, parsed_by])
    else :
        pygame.draw.line(Window, COLOR_WHITE, [parsed_bx, parsed_sy], [parsed_bx, parsed_ey])
    pygame.display.update()

def draw_gap_grid (Window, Sx, Sy, Ex, Ey, Direction, Bx, By) :
    # Parse the grid coordinates to the display coordinates.
    parsed_sx = CELL_W * (Sx + 1)
    parsed_sy = CELL_W * (Sy + 1)
    parsed_ex = CELL_W * (Ex + 1)
    parsed_ey = CELL_W * (Ey + 1)
    parsed_bx = CELL_W * (Bx + 1)
    parsed_by = CELL_W * (By + 1)
    random_x = random.randrange(parsed_sx, parsed_ex, CELL_W)
    random_y = random.randrange(parsed_sy, parsed_ey, CELL_W)
    if Direction == HORIZONTAL :
        pygame.draw.line(Window, COLOR_BLUE, [random_x + 1, parsed_by], [random_x + CELL_W - 1, parsed_by])
    else :
        pygame.draw.line(Window, COLOR_BLUE, [parsed_bx, random_y + 1], [parsed_bx, random_y + CELL_W - 1])
    pygame.display.update()

def draw_fill_grid_color(Window, Color, Width, Height) :
    pygame.draw.rect(Window, Color, (CELL_W + 1, CELL_W + 1, (CELL_W * Width) - 1, (CELL_W * Height) - 1), 0)

def draw_cell(Window, X, Y, Color) :
    pygame.draw.rect(Window, Color, (X + 1, Y + 1, 19, 19), 0)
    pygame.display.update()

def draw_fill_start_and_end_cells(Window, Width, Height) :
    draw_cell(Window, CELL_W, CELL_W, COLOR_RED)
    draw_cell(Window, CELL_W * Width, CELL_W * Height, COLOR_RED)

def draw_next_cell(Window, X, Y, Direction, Color) :
    # Go to the top cell
    if(Direction == 'up') :
        pygame.draw.rect(Window, Color, (X + 1, Y - CELL_W + 1, 19, 39), 0)
    # Go to the left cell
    elif(Direction == 'left') :
        pygame.draw.rect(Window, Color, (X - CELL_W + 1, Y + 1, 39, 19), 0)
    # Go to the bottom cell
    elif(Direction == 'down') :
        pygame.draw.rect(Window, Color, (X + 1, Y + 1, 19, 39), 0)
    # Go to the right cell
    elif(Direction == 'right') :
        pygame.draw.rect(Window, Color, (X + 1, Y + 1, 39, 19), 0)
    pygame.display.update()

def draw_next_cell_line(Window, X, Y, Direction, Color) :
    # Go to the top cell
    if(Direction == 'up') :
        pygame.draw.rect(Window, Color, (X + 1, Y - CELL_W + 1, 19, 20), 0)
    # Go to the left cell
    elif(Direction == 'left') :
        pygame.draw.rect(Window, Color, (X - CELL_W + 1, Y + 1, 20, 19), 0)
    # Go to the bottom cell
    elif(Direction == 'down') :
        pygame.draw.rect(Window, Color, (X + 1, Y + 1, 19, 20), 0)
    # Go to the right cell
    elif(Direction == 'right') :
        pygame.draw.rect(Window, Color, (X + 1, Y + 1, 20, 19), 0)
    pygame.display.update()

def draw_cells(Window, Start_x, Start_y, End_x, End_y, Color) :
    pygame.draw.rect(Window, Color, (Start_x + 1, Start_y + 1, End_x - Start_x - 1, End_y - Start_y - 1), 0)

def getCellWidth() :
    return CELL_W