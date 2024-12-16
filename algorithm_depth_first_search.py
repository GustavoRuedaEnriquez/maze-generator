"""
--------------------------------
| Maze-Generator               |
| Depth first search algorithm |
-------------------------------
Author: Gustavo Adolfo Rueda Enríquez
Python 3.8
"""

import random
import utils.draw as Draw

# START_X
START_X = 1
# START_Y
START_Y = 1

# CELLS ARRAY
stack   = []
visited = []

"""
Checks if a certain cell from the maze matrix has neighbors on at least 1 out of
4 possible directions (above, left, below, right). Returns True if cell has at
least a neighbor directly adjacent to it.
"""

def has_neighbors(matrix, position):
  x = position[0]
  y = position[1]

  # Since walls also occupies one cell, to check ih a cell has neighbors, we
  # have to move "one distance unit" (odu), which is equal to 2 cells
  odu =  2

  top = False
  left = False
  bottom = False
  right = False

  # Check cell from above
  if (y - odu > 0):
    top = ((x, y-odu) not in visited) and (matrix[y-odu][x] == Draw.SLOT_CONST)
  
  # Check cell from the left
  if (x - odu > 0):
    left = ((x-odu, y) not in visited) and (matrix[y][x-odu] == Draw.SLOT_CONST)
  
  # Check cell from below
  if (y + odu < len(matrix)):
    bottom = ((x, y+odu) not in visited) and (matrix[y+odu][x] == Draw.SLOT_CONST)

  # Check cell from the right
  if (x + odu < len(matrix[y])):
    right = ((x+odu, y) not in visited) and (matrix[y][x+odu] == Draw.SLOT_CONST)

  return top or left or bottom or right

"""
Searchs for all neighbors a certain cell from the maze matrix could have, a cell
could have at most 1 neighbor on 4 possible directions (above, left, below,
right). Returns a dictionary array with all existing neighbors. Dictionaries
have the following structure:
{
  'dir':'left',
  'coords' : (X, Y)
}
"""

def get_neighbors(matrix, position):
  x = position[0]
  y = position[1]
  available_neighbors = []

  # Since walls also occupies one cell, to check ih a cell has neighbors, we
  # have to move "one distance unit" (odu), which is equal to 2 cells
  odu =  2

  # Check cell from above
  if (y - odu > 0):
    if ((x, y-odu) not in visited) and (matrix[y-odu][x] == Draw.SLOT_CONST):
      coords = (x, y - odu)
      available_neighbors.append({'dir':'top', 'coords': coords})
  
  # Check cell from left
  if (x - odu > 0):
    if ((x-odu, y) not in visited) and (matrix[y][x-odu] == Draw.SLOT_CONST):
      coords = (x - odu, y)
      available_neighbors.append({'dir':'left', 'coords': coords})

  # Check cell from below
  if (y + odu < len(matrix)):
    if ((x, y+odu) not in visited) and (matrix[y+odu][x] == Draw.SLOT_CONST):
      coords = (x, y + odu)
      available_neighbors.append({'dir':'bottom', 'coords': coords})
  
  # Check cell from right
  if (x + odu < len(matrix[y])):
    if ((x+odu, y) not in visited) and (matrix[y][x+odu] == Draw.SLOT_CONST):
      coords = (x + odu, y)
      available_neighbors.append({'dir':'right', 'coords': coords})
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
  cur_x = a_x + dir_x
  cur_y = a_y + dir_y

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
  Draw.draw_connecting_cells(window, matrix, slot_a, slot_b, Draw.COLOR_VIOLET)

"""
Function that executes the whole DFS algorithm, this function will modify the
matrix and also draw the maze.
"""

def draw_dfs_algorithm(window, matrix, width, height):
  # Draw our starting point and append it to the cells stack and visited
  # cells array
  Draw.draw_maze_cell(window, matrix, (START_X,START_Y), Draw.COLOR_GREEN)
  stack.append((START_X, START_Y))
  visited.append((START_X, START_Y))

  coord_x = START_X
  coord_y = START_Y

  while(len(stack) > 0):
    # Check which neighbors are available.
    available_cells = get_neighbors(matrix, (coord_x, coord_y))
        
    # Select a random neighbor and move the cell to it.
    if(len(available_cells) != 0) :
      next_cell = random.choice(available_cells)
      connect_slots(window, matrix, (coord_x, coord_y), next_cell['coords'])
            
      if(next_cell['dir'] == 'top' or next_cell['dir'] == 'bottom'):
        coord_y = next_cell['coords'][1]
      elif(next_cell['dir'] == 'left' or next_cell['dir'] == 'right') :
        coord_x = next_cell['coords'][0]

      visited.append(next_cell['coords'])
      stack.append(next_cell['coords'])

      # Mark the new current cell's position
      Draw.draw_maze_cell(window, matrix, (coord_x, coord_y), Draw.COLOR_GREEN)
    else :
      # Mark current cell as part of the maze
      Draw.draw_maze_cell(window, matrix, (coord_x, coord_y), Draw.COLOR_CYAN)
            
      # Re-draw the backtracked path, peeking if the previous element had
      # neighbors, if it does not have any neighbors, mark it as part of the
      # maze. Continue with the neighbors otherwise.
      old_x, old_y = coord_x, coord_y
      if(has_neighbors(matrix, stack[-1]) != True):
        coord_x, coord_y = stack.pop()
        # Re-draw right path
        if(old_x != coord_x):
          Draw.draw_connecting_cells(window, matrix, (coord_x, coord_y), (old_x, coord_y), Draw.COLOR_CYAN)
        elif(old_y != coord_y) :
          Draw.draw_connecting_cells(window, matrix, (coord_x, coord_y), (coord_x, old_y), Draw.COLOR_CYAN)
      else :
        coord_x, coord_y = stack[-1][0], stack[-1][1]
        if(old_x != coord_x) :
          Draw.draw_connecting_cells(window, matrix, (coord_x, coord_y), (old_x, coord_y), Draw.COLOR_CYAN)
        elif(old_y != coord_y) :
          Draw.draw_connecting_cells(window, matrix, (coord_x, coord_y), (coord_x, old_y), Draw.COLOR_CYAN)            
  Draw.draw_start_end_cells(window, matrix, width, height)

"""
Entry point of the algorithm, this is the function that maze.py calls
"""

def generate_maze(window, maze_matrix, width, height) :
  Draw.draw_maze_matrix(window, maze_matrix)
  draw_dfs_algorithm(window, maze_matrix, width, height)
  