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

import pygame

# WALL CONSTANT
WALL_CONST = 0

# SLOT CONSTANT
SLOT_CONST = 1

# GUI WINDOW DIMENSIONS
SCREEN_W = 800
SCREEN_H = 800

# CELL WIDTH (SQUARE CELLS)
CELL_W = 9

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
COLOR_CYAN   = (0, 183, 235)
COLOR_VIOLET = (238, 130, 238)

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

def draw_start_end_cells(Window, matrix, width, height):
  start = (1,1)
  end = ((2 * width - 1), (2 * height - 1))
  draw_maze_cell(Window, matrix, start, COLOR_BLUE)
  draw_maze_cell(Window, matrix, end, COLOR_BLUE)
  pygame.display.update()

def draw_maze_matrix(Window, maze_matrix, slot_color):
  y = Y_0
  for i in range(0, len(maze_matrix)):
    x = X_0
    for j in range(0, len(maze_matrix[i])):
      cell = pygame.Rect([x, y], [CELL_W, CELL_W])
      if maze_matrix[i][j] is WALL_CONST:
        pygame.draw.rect(Window, COLOR_GRAY, cell)
      elif maze_matrix[i][j] is SLOT_CONST:
        pygame.draw.rect(Window, slot_color, cell)
      x += CELL_W
    y += CELL_W
  pygame.display.update()

def draw_maze_cell(Window, maze_matrix, coords, color):
  coord_x = coords[0]
  coord_y = coords[1]

  y = Y_0
  for i in range(0, len(maze_matrix)):
    x = X_0
    for j in range(0, len(maze_matrix[i])):
      cell = pygame.Rect([x, y], [CELL_W, CELL_W])
      if i == coord_y and j == coord_x:
        pygame.draw.rect(Window, color, cell)
      x += CELL_W
    y += CELL_W
  pygame.display.update()

def draw_connecting_cells(Window, maze_matrix, cell_a, cell_b, color):
  # X, Y components of both slots to merge
  a_x = cell_a[0]
  a_y = cell_a[1]
  b_x = cell_b[0]
  b_y = cell_b[1]

  # Delta X and Delta Y
  dx = b_x - a_x
  dy = b_y - a_y

  # Direction of the delta
  if dx == 0:
    dir_x = 0
  elif dx > 0:
    dir_x = 1
  else:
    dir_x = -1

  if dy == 0:
    dir_y = 0
  elif dy > 0:
    dir_y = 1
  else:
    dir_y = -1

  draw_maze_cell(Window, maze_matrix, (a_x, a_y), color)
  cur_x = a_x + dir_x
  cur_y = a_y + dir_y

  # Draw all the cells between slot A and slot B (including slot B) with
  # specified color
  for i in range(0, abs(dx)):
    draw_maze_cell(Window, maze_matrix, (cur_x, cur_y), color)
    cur_x += dir_x

  for i in range(0, abs(dy)):
    draw_maze_cell(Window, maze_matrix, (cur_x, cur_y), color)
    cur_y += dir_y

  pygame.display.update()

def draw_outer_perimeter (window, width, height) :
  x = X_0
  y = Y_0

  # Fill all space with a solid color
  cell = pygame.Rect([x, y], [(2*width+1) * CELL_W, (2*height+1) *  CELL_W])
  pygame.draw.rect(window, COLOR_CYAN, cell)

  # Top line margin
  cell = pygame.Rect([x, y], [(2 * width + 1) * CELL_W, CELL_W])
  pygame.draw.rect(window, COLOR_GRAY, cell)

  # Left line margin
  cell = pygame.Rect([x, y], [CELL_W, (2 * height + 1) * CELL_W])
  pygame.draw.rect(window, COLOR_GRAY, cell)

  # Bottom line margin
  x = X_0 + (2 * width* CELL_W)
  y = Y_0
  cell = pygame.Rect([x, y], [CELL_W, (2 * height + 1) * CELL_W])
  pygame.draw.rect(window, COLOR_GRAY, cell)

  # Right line margin
  x = X_0
  y = Y_0 + (2 * height * CELL_W)  
  cell = pygame.Rect([x, y], [(2 * width + 1) * CELL_W, CELL_W])
  pygame.draw.rect(window, COLOR_GRAY, cell)

  pygame.display.update()

def cut_maze(window, start, end, column_nth, direction):
  start_x = start[0]
  start_y = start[1]
  end_x = end[0]
  end_y = end[1]

  x = X_0 + (start_x * CELL_W)
  y = Y_0 + (start_y * CELL_W)

  if (direction == 'vertical'):
    x += CELL_W * (column_nth - start_x)
    cell = pygame.Rect([x, y], [CELL_W, (end_y - start_y) * CELL_W])
  elif (direction == 'horizontal'):
    y += CELL_W * (column_nth - start_y)
    cell = pygame.Rect([x, y], [ (end_x - start_x) * CELL_W, CELL_W])

  pygame.draw.rect(window, COLOR_GRAY, cell)
  pygame.display.update()