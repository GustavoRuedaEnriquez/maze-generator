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

all_rows = dict()
current_row = dict()

def generate_maze(window, maze_matrix, width, height) :
  Draw.draw_maze_matrix(window, maze_matrix, Draw.COLOR_WHITE)
  #execute_eller_algorithm(window, maze_matrix, width, height)