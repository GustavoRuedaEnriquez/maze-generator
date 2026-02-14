"""
--------------------------------
| Maze-Generator               |
| Eller's algorithm            |
-------------------------------
Author: Gustavo Adolfo Rueda Enríquez
Python 3.8

"""

import random
import utils.draw as Draw

# We will store the sets of the row on dictionaries.
row_sets = dict()

# This array will contain all cell that are not orphan, this meaning, cells that
# belong to a set.
non_orphan_cells = list()

"""
Function that merges 2 sets.
"""

def merge_sets(set_1_id, set_2_id):
  row_sets[set_1_id] = row_sets[set_1_id].union(row_sets[set_2_id])
  del row_sets[set_2_id]  

"""
Function that helps us find the set id of the set that contains certain cell
coordinates.
"""

def find_set_with_cell(cell):
  for key in row_sets.keys():
    if cell in row_sets[key]:
      return key
  return None

"""
First step of Eller's algorithm, randomly merge adjacent disjoint cells, this
function will modify the matrix and also draw on the grid to reflect these
merges/connections
"""

def merge_adjacent_sets(window, matrix, width, height, curr_y):
  keep_processing = True
  curr_x = 1

  # Since walls also occupies one cell, to check if a cell has neighbors, we
  # have to move "one distance unit" (odu), which is equal to 2 cells
  odu = 2

  while keep_processing:
    # Stop processing when we reach the last column
    if curr_x >= 2 * width - 1:
      keep_processing = False
      break

    # Check if neighbor cell does not belong on same set.
    set_id = find_set_with_cell((curr_x, curr_y))

    # If we are on the last row, we need to connect all adjacent cells
    if curr_y == 2 * height - 1:
      if (curr_x + odu, curr_y) not in row_sets[set_id]:
        other_set_id = find_set_with_cell((curr_x + odu, curr_y))
        merge_sets(set_id, other_set_id)
        start = (curr_x, curr_y)
        end = (curr_x + odu, curr_y)

        # Modify the matrix cell to reflect this connection
        matrix[curr_y][curr_x] = 1
        matrix[curr_y][curr_x + 1] = 1
        matrix[curr_y][curr_x + odu] = 1

        # Draw the cells connection
        Draw.draw_connecting_cells(window, matrix, start, end, Draw.COLOR_CYAN)
      else:
        curr_x += odu

    # Can we join these 2 neighbor cells?
    elif (curr_x + odu, curr_y) not in row_sets[set_id]:
      # Are we going to merge the cells (union both sets)?
      merge_set_factor = random.randint(0,1)
      if merge_set_factor:
        other_set_id = find_set_with_cell((curr_x + odu, curr_y))
        merge_sets(set_id, other_set_id)
        start = (curr_x, curr_y)
        end = (curr_x + odu, curr_y)

        # Modify the matrix cell to reflect this connection
        matrix[curr_y][curr_x] = 1
        matrix[curr_y][curr_x + 1] = 1
        matrix[curr_y][curr_x + odu] = 1

        # Draw the cells connection
        Draw.draw_connecting_cells(window, matrix, start, end, Draw.COLOR_CYAN)
      else:
        curr_x += odu
  
    else:
      curr_x += odu

  # TODO: Modify matrix.  

"""
Second step of Eller's algorithm, from the resulting merged sets from step 1,
randomly merge cells from below (at least one per set), this function will
modify the matrix and also draw on the grid to reflect these merges/connections.
"""

def choose_cells_from_below(window, matrix):
  # For each set, choose random cells from next row
  for key in row_sets.keys():
    # Set a random number of openings
    num_cells = random.randint(1, len(row_sets[key]))
    chosen_cells = list()
    # Remove all coordinates from the set, since their row has already been
    # processed.
    while len(row_sets[key]) > 0:
      cell = row_sets[key].pop()
      non_orphan_cells.remove(cell)
      if num_cells > 0:
        chosen_cells.append(cell)
        num_cells -= 1

    # Add the cells from below chosen to the same set. Since walls also occupies
    # one cell, to point to a cell on the next row we have to move "one distance
    # unit" (odu), which is equal to 2 cells
    odu =  2
    for i in range(0, len(chosen_cells)):
      x = chosen_cells[i][0]
      y = chosen_cells[i][1]
      row_sets[key].add((x, y + odu))
      non_orphan_cells.append((x, y + odu))

      # Modify the matrix cell to reflect this connection
      matrix[y][x] = 1
      matrix[y + 1][x] = 1
      matrix[y + odu][x] = 1

      # Draw the cells connection
      Draw.draw_connecting_cells(window, matrix,(x,y),(x,y+odu),Draw.COLOR_CYAN)

"""
Function that executes the whole Eller's algorithm, this function will modify
the matrix and also draw the maze.
"""

def execute_eller_algorithm(window, matrix, width, height):
  set_id = 1

  current_x = 1
  current_y = 1

  # For each slot on 1st row, create a set and add slot coordinates on it.
  # Slot cells are always odd cells on X and odd on Y.
  for i in range (1, width + 1):
    current_x = 2 * i - 1
    row_sets[set_id] = {(current_x, current_y)}
    non_orphan_cells.append((current_x, current_y))
    set_id += 1
  
  for i in range (0, height):
    merge_adjacent_sets(window, matrix, width, height, current_y)
    #time.sleep(6)
    # Skip these steps when being on the last row
    if (current_y < 2 * height - 1):
      choose_cells_from_below(window, matrix)
      #time.sleep(6)
      current_y += 2
      # Add any possible orphan cell to a unique set
      for i in range (1, width + 1):
       current_x = 2 * i - 1
       if (current_x, current_y) not in non_orphan_cells:
          row_sets[set_id] = {(current_x, current_y)}
          non_orphan_cells.append((current_x, current_y))
          set_id += 1
          
  Draw.draw_start_end_cells(window, matrix, width, height)
  
"""
Entry point of the algorithm, this is the function that maze.py calls
"""

def generate_maze(window, maze_matrix, width, height) :
  Draw.draw_maze_matrix(window, maze_matrix, Draw.COLOR_WHITE)
  execute_eller_algorithm(window, maze_matrix, width, height)