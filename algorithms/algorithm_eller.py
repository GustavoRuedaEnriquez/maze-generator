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

# We will store the sets on dictionaries, one will consider all cells from all
# rows, another one will focus only on the processed row.
all_rows = dict()
current_row = dict()

def merge_sets(dictionary, set_1_id, set_2_id, set_ids):
  print("\nWill merge set ", set_1_id, " with set ", set_2_id)
  print("dict before merging: ", dictionary)

  dictionary[set_1_id] = dictionary[set_1_id].union(dictionary[set_2_id])
  del dictionary[set_2_id]
  set_ids.remove(set_2_id)
  
  print("dict after merging: ", dictionary)
  

def is_set_on_right_end(cell_set, width):
  last_right_cell = (1,1)
  #print(last_right_cell[0])
  for cell in cell_set:
    #print(cell[0])
    if cell[0] > last_right_cell[0]:
      last_right_cell = cell
  
  if last_right_cell[0] == (2 * width -1):
    return True
  else:
    return False


def random_merge_adjacent_sets(width):
  set_ids = list(current_row.keys())
  sets_on_row = len(set_ids)

  # Determine how many sets are going to be merged
  sets_to_merge = random.randint(1, sets_on_row - 1)
  print("Will do ", sets_to_merge, " merge(s)\n")

  while sets_to_merge > 0:
    print(set_ids)
    # Randomly choose a set id
    id = random.choice(set_ids)
    id_idx = set_ids.index(id)

    # Check if the set is located on the right end, if this is the case, we will
    # merge with the set from the left, otherwise we merge with the set from the
    # right
    if is_set_on_right_end(current_row[id], width):
      # Merge with left set
      merge_sets(current_row, set_ids[id_idx], set_ids[id_idx - 1], set_ids)
    else:
      # Merge with right set
      merge_sets(current_row, set_ids[id_idx], set_ids[id_idx + 1], set_ids)
    
    sets_to_merge -= 1

def execute_eller_algorithm(window, maze_matrix, width, height):
  set_id = 1

  current_x = 1
  current_y = 1

  # For each slot on 1st row, create a set and add slot coordinates on it.
  # Slot cells are always odd cells on X and odd on Y.
  for i in range (1, width + 1):
    current_x = 2 * i - 1
    all_rows[set_id] = {(current_x, current_y)}
    current_row[set_id] = {(current_x, current_y)}
    set_id += 1
  
  #print("all_rows\n",all_rows)
  #print("current_row\n",current_row)

  # Randomly merge adjacent cells that belong to different sets
  random_merge_adjacent_sets(width)

def generate_maze(window, maze_matrix, width, height) :
  Draw.draw_maze_matrix(window, maze_matrix, Draw.COLOR_WHITE)
  execute_eller_algorithm(window, maze_matrix, width, height)