"""
--------------------------------
| Maze-Generator               |
| Kruskal's algorithm          |
-------------------------------
Author: Gustavo Adolfo Rueda Enríquez
Python 3.8

"""

import random
import utils.draw as Draw

# CELLS ARRAY
edges = []

def create_sets(width, height):
  sets = []

  for i in range(1, height + 1):  
    for j in range (1, width + 1):
      x = 2 * j - 1
      y = 2 * i - 1
      temp = set()
      temp.add((x,y))
      sets.append(temp)

  return sets

def populate_edges_array(width, height):
  for i in range(1, height + 1):  
    for j in range (1, width + 1):
        x = 2 * j - 1
        y = 2 * i - 1
        edges.append((x,y))

def on_same_set(position_1, position_2, sets):
  x1 = position_1[0]
  y1 = position_1[1]
  x2 = position_2[0]
  y2 = position_2[1]

  # Check if a position 1 is on the same set as position 2
  for Set in sets :
    if (x1, y1) in Set  and (x2, y2) in Set:  
      return True
  return False

def merge_sets(position_1, position_2, sets):
  idx_pos_1 = 0
  idx_pos_2 = 0
  set_1 = {}
  set_2 = {}

  # Get set where position_1 is located 
  for Set in sets:
    if (position_1 in Set):  
      set_1 = set(Set)
      break
    idx_pos_1 += 1

  # Get set where position_2 is located
  for Set in sets:
    if (position_2 in Set):  
      set_2 = set(Set)
      break
    idx_pos_2 += 1

  # Remove the 2 sets from the sets array
  sets.pop(idx_pos_1)
  if(idx_pos_1 < idx_pos_2):
    sets.pop((idx_pos_2-1))
  else:
    sets.pop(idx_pos_2)

  # Create a new set containing both positions and add it to the sets array
  new_set = set()
  new_set = new_set.union(set_1)
  new_set = new_set.union(set_2)

  sets.append(new_set)


def obtain_disjoint_neighbor(matrix, sets, position):
  candidates = []

  # Since walls also occupies one cell, to check if a cell has neighbors, we
  # have to move "one distance unit" (odu), which is equal to 2 cells
  odu =  2
  x = position[0]
  y = position[1]

  neighbor_coord = None

  # Check cell from above
  if (y - odu > 0):
    if (on_same_set((x,y), (x,y-odu), sets) == False):
      candidates.append('top')

  # Check cell from left
  if (x - odu > 0):
    if (on_same_set((x,y), (x-odu,y), sets) == False):
      candidates.append('left')

  # Check cell from below
  if (y + odu < len(matrix)):
    if (on_same_set((x,y), (x,y+odu), sets) == False):
      candidates.append('bottom')

  # Check cell from right
  if (x + odu < len(matrix)):
    if (on_same_set((x,y), (x+odu,y), sets) == False):
      candidates.append('right')

  # Select randomly one of the candidates
  if(len(candidates) == 0):
    neighbor = None
  else:
    # Returns the coordinates of the chosen neighbor, merge both sets
    neighbor = random.choice(candidates)
    if (neighbor == 'top'):
      merge_sets((x, y), (x, y-odu), sets)
      neighbor_coord = (x, y-odu)
    elif( neighbor == 'left') :
      merge_sets((x, y), (x-odu, y), sets)
      neighbor_coord = (x-odu, y)
    elif( neighbor == 'bottom') :
      merge_sets((x, y), (x, y+odu), sets)
      neighbor_coord = (x, y+odu)
    elif( neighbor == 'right') :
      merge_sets((x, y), (x+odu, y), sets)
      neighbor_coord = (x+odu, y)

  return neighbor_coord


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

def execute_kruskal_algorithm(window, matrix, width, height) :
  # Add all the slots to set and edges array.
  sets = create_sets(width, height)
  populate_edges_array(width, height)
  random.shuffle(edges)
    
  index = 0
  total_sets = len(sets)

  while(len(sets) > 1) :    
    # Select an edge at random and search for a neighboring edge.
    x, y = edges[index]
    neighbor = obtain_disjoint_neighbor(matrix, sets, (x, y))

    if( neighbor != None ) :
        connect_slots(window, matrix, (x,y), neighbor)
    index = (index + 1) % total_sets

  Draw.draw_start_end_cells(window, matrix, width, height)

def generate_maze(window, maze_matrix, width, height) :
  Draw.draw_maze_matrix(window, maze_matrix, Draw.COLOR_WHITE)
  execute_kruskal_algorithm(window, maze_matrix, width, height)
