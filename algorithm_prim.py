"""
--------------------------------
| Maze-Generator               |
| Prim's algorithm             |
-------------------------------
Author: Gustavo Adolfo Rueda Enríquez
Python 3.8

"""

import random
import utils.draw as Draw

# CELLS ARRAY
maze = set()
frontiers = set()

def get_random_slot(width, height):
  rand_x = random.randint(1, width)
  rand_y = random.randint(1, height)
  coord_x = 2 * rand_x - 1
  coord_y = 2 * rand_y - 1
  return (coord_x, coord_y)

def get_frontiers(window, matrix, position):
  x = position[0]
  y = position[1]
  available_frontiers = []

  # Since walls also occupies one cell, to check if a cell has neighbors, we
  # have to move "one distance unit" (odu), which is equal to 2 cells
  odu =  2

  # Check cell from above
  if (y - odu > 0):
    if ((x, y-odu) not in frontiers) and (matrix[y-odu][x] == Draw.SLOT_CONST) \
        and ((x, y-odu) not in maze):
      coords = (x, y - odu)
      available_frontiers.append(coords)
      Draw.draw_maze_cell(window, matrix, coords, Draw.COLOR_GREEN)
  
  # Check cell from left
  if (x - odu > 0):
    if ((x-odu, y) not in frontiers) and (matrix[y][x-odu] == Draw.SLOT_CONST) \
        and ((x-odu, y) not in maze):
      coords = (x - odu, y)
      available_frontiers.append(coords)
      Draw.draw_maze_cell(window, matrix, coords, Draw.COLOR_GREEN)

  # Check cell from below
  if (y + odu < len(matrix)):
    if ((x, y+odu) not in frontiers) and (matrix[y+odu][x] == Draw.SLOT_CONST) \
        and ((x, y+odu) not in maze):
      coords = (x, y + odu)
      available_frontiers.append(coords)
      Draw.draw_maze_cell(window, matrix, coords, Draw.COLOR_GREEN)
  
  # Check cell from right
  if (x + odu < len(matrix[y])):
    if ((x+odu, y) not in frontiers) and (matrix[y][x+odu] == Draw.SLOT_CONST) \
        and ((x+odu, y) not in maze):
      coords = (x + odu, y)
      available_frontiers.append(coords)
      Draw.draw_maze_cell(window, matrix, coords, Draw.COLOR_GREEN)

  return available_frontiers

def get_neighbor_maze_slots(matrix, position):
  x = position[0]
  y = position[1]
  available_neighbors = []

  # Since walls also occupies one cell, to check if a cell has neighbors, we
  # have to move "one distance unit" (odu), which is equal to 2 cells
  odu =  2

  # Check cell from above
  if (y - odu > 0):
    if ((x, y-odu) in maze) and (matrix[y-odu][x] == Draw.SLOT_CONST):
      coords = (x, y - odu)
      available_neighbors.append(coords)
  
  # Check cell from left
  if (x - odu > 0):
    if ((x-odu, y) in maze) and (matrix[y][x-odu] == Draw.SLOT_CONST):
      coords = (x - odu, y)
      available_neighbors.append(coords)

  # Check cell from below
  if (y + odu < len(matrix)):
    if ((x, y+odu) in maze) and (matrix[y+odu][x] == Draw.SLOT_CONST):
      coords = (x, y + odu)
      available_neighbors.append(coords)
  
  # Check cell from right
  if (x + odu < len(matrix[y])):
    if ((x+odu, y) in maze) and (matrix[y][x+odu] == Draw.SLOT_CONST):
      coords = (x + odu, y)
      available_neighbors.append(coords)

  return available_neighbors

"""
Changes the maze matrix to reflect a connection between 2 slots. Also the one in
charge to draw this new connection between cells
"""

def connect_slots(window, matrix, slot_a, slot_b):
  # X, Y components of both slots to merge
  a_x = slot_a[0]
  a_y = slot_a[1]
  b_x = slot_b[0]
  b_y = slot_b[1]

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

  matrix[a_y][a_x] = Draw.SLOT_CONST
  cur_x = a_x
  cur_y = a_y

  # Set all the cells between slot A and slot B (including slot B) as free slots
  if (dx != 0):
    for i in range(0, abs(dx)):
      matrix[cur_y][cur_x] = Draw.SLOT_CONST
      cur_x += dir_x

  if (dy != 0):
    for i in range(0, abs(dy)):
      matrix[cur_y][cur_x] = Draw.SLOT_CONST
      cur_y += dir_y

  # Draw the change we have just made on the maze matrix
  Draw.draw_connecting_cells(window, matrix, slot_a, slot_b, Draw.COLOR_CYAN)

def execute_prim_algorithm(window, matrix, width, height):
  # Choose random slot on the matrix.
  start =  get_random_slot(width, height)
  maze.add(start)
  Draw.draw_maze_cell(window, matrix, start, Draw.COLOR_CYAN)

  # Search for the possible frontiers around our starting slot.
  available_frontiers = get_frontiers(window, matrix, start)
  frontiers.update(available_frontiers)

  while(len(frontiers) > 0) :
    # Obtain a random frontier slot.
    frontier = frontiers.pop()
    x = frontier[0]
    y = frontier[1]

    # Search for a neighbor neighbor slot that is already part of the maze.
    neighbors = get_neighbor_maze_slots(matrix, (x, y))

    # Choose a random neighbor on the maze and merge it with the frontier slot
    if(len(neighbors) > 0) :
      neighbor = random.choice(neighbors)
      connect_slots(window, matrix, (x, y), neighbor)

      # Add the frontier slot to the maze array, this is done to mark it as
      # processed
      maze.add((x, y))

      # Add all neighboring frontiers of the recently processed slot found to
      # the frontiers set.
      frontiers.update(get_frontiers(window, matrix, (x, y)))

  Draw.draw_start_end_cells(window, matrix, width, height)
            
def generate_maze(window, maze_matrix, width, height) :
    Draw.draw_maze_matrix(window, maze_matrix)
    execute_prim_algorithm(window, maze_matrix, width, height)