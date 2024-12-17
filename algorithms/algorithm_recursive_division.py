"""
--------------------------------
| Maze-Generator               |
| Recursive Division algorithm |
-------------------------------
Author: Gustavo Adolfo Rueda Enríquez
Python 3.8

"""

import random
import utils.draw as Draw

'''
Function in charge of doing a cut vertically or horizontally across a section of
the maze. This function will modify the maze matrix and also draw the cut on
screen
'''

def cut_maze(window, matrix, direction, start, end, coord_x, coord_y):
  start_x = start[0]
  start_y = start[1]
  end_x = end[0]
  end_y = end[1]

  if (direction == 'vertical'):
    for i in range(start_y, end_y):
      # Set all matrix slots alongside (coord_x, *) as walls.
      matrix[i][coord_x] = Draw.WALL_CONST
    # Reflect the maze cut by drawing the wall
    Draw.cut_maze(window, start, end, coord_x, direction)

  elif (direction == 'horizontal'):
    for i in range(start_x, end_x):
      # Set all matrix slots alongside (*, coord_y) as walls.
      matrix[coord_y][i] = Draw.WALL_CONST
    # Reflect the maze cut by drawing the wall
    Draw.cut_maze(window, start, end, coord_y, direction)

'''
Function that creates a gap on the wall done by cut_maze function, this gap will
allow to mantain connectability on the graph. This function will modify the maze
matrix and also draw the gap on screen
'''

def create_gap(window, matrix, direction, start, end, col_x, row_y):
  start_x = start[0]
  start_y = start[1]
  end_x = end[0]
  end_y = end[1]
  # Choose randomly one slot cell from maze metrics that is on the cutting
  # wall path. Slot cells are always odd cells.
  if (direction == 'vertical'):
    # Choose a random y coordinate, it must be odd.
    while True:
      y = random.randrange(start_y, end_y)
      if (y % 2 != 0):
        break
    x_coord = col_x
    y_coord = y

  elif (direction == 'horizontal'):
    # Choose a random x coordinate, it must be odd.
    while True:
      x = random.randrange(start_x, end_x)
      if (x % 2 != 0):
        break
    x_coord = x
    y_coord = row_y

  # Set the cell as a usable slot instead of a wall
  matrix[y_coord][x_coord] = Draw.SLOT_CONST
    
  # Draw the new usable slot
  Draw.draw_maze_cell(window, matrix, (x_coord, y_coord), Draw.COLOR_CYAN)

'''
Recursive function that will cut the maze, create a gap and continue again until
no more cuts can be done on the maze.
'''

def bisect_maze(window, matrix, start, end, width, height):
  start_x = start[0]
  start_y = start[1]
  end_x = end[0]
  end_y = end[1]

  # Calculate free work area, this mean, how many cuts can be done vertically
  # or horizontally in the area.
  possible_cuts_x = (end_x - start_x) // 2
  possible_cuts_y = (end_y - start_y) // 2

  # Stop condition, if there are less than 1 cut available, stop recursion.
  if possible_cuts_x < 1 or possible_cuts_y < 1:
    return
  
  # Choose cut directiony
  if possible_cuts_y > possible_cuts_x:
    direction = 'horizontal'
  elif possible_cuts_x > possible_cuts_y:
    direction = 'vertical'
  else:
    i = random.randint(0,1)
    direction = 'vertical' if i==0 else 'horizontal'

  # Select the cut point, we will choose randomly a wall cell from the matrix.
  # Wall cells are always located on even cell on the matrix.
  while True:
    cut_col_x = random.randrange(start_x, end_x)
    if (cut_col_x % 2 == 0):
      break
  while True:
    cut_row_y = random.randrange(start_y, end_y)
    if (cut_row_y % 2 == 0):
      break
  
  # Cut maze
  cut_maze(window, matrix, direction, start, end, cut_col_x, cut_row_y)
  
  # Create a 'hallway' that passes through the cut we have just done to preserve
  # connectability
  create_gap(window, matrix, direction, start, end, cut_col_x, cut_row_y)
  
  # Prepare for next iteration
  if direction == 'horizontal':
    bisect_maze(window, matrix, (start_x, start_y), (end_x, cut_row_y), width, height)
    bisect_maze(window, matrix, (start_x,cut_row_y+1), (end_x, end_y), width, height)
  else:
    bisect_maze(window, matrix, (start_x, start_y), (cut_col_x, end_y), width, height)
    bisect_maze(window, matrix, (cut_col_x+1,start_y), (end_x, end_y), width, height)

"""
Function that executes the whole recursive division algorithm.
"""

def exec_recursive_division_algorithm(window, matrix, width, height) :
  bisect_maze(window, matrix, (1, 1), (width * 2, height * 2), width, height)
  Draw.draw_start_end_cells(window, matrix, width, height)

"""
Entry point of the algorithm, this is the function that maze.py calls
"""

def generate_maze(window, maze_matrix, width, height) :
  Draw.draw_outer_perimeter (window, width, height)
  exec_recursive_division_algorithm(window, maze_matrix, width, height)