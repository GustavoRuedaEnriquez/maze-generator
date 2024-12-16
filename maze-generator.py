# pylint: disable=no-member

"""
--------------------------------
| Maze-Generator               |
| Main program                 |
-------------------------------
Author: Gustavo Adolfo Rueda Enríquez
Python 3.8

"""

import sys
import maze
import algorithm_depth_first_search as Dfs
import algorithm_prim as Prim
import algorithm_kruskal as Kruskal
import algorithm_recursive_division as RecursiveDivision

algorithms = ['dfs', 'prim', 'kruskal', 'recursive-div']

def print_error(Message) :
    print()
    print(Message)
    print()
    print('Usage:') 
    print('\tpython maze-generator.py [WIDTH] [HEIGHT] [ALGORITHM]')
    print('\tWIDTH  - The number of cells alongside the width.  The valid values are [5 - 30]')
    print('\tHEIGHT - The number of cells alongside the height. The valid values are [5 - 30]')
    print('\tALGORITHM - The desired maze generation algorithm to use. The valid options are:')
    print('\t\tdfs.............Depth First Search algorithm.')
    print('\t\tprim............Prim\'s algorithm.')
    print('\t\tkruskal.........Kruskal\'s algorithm.')
    print('\t\trecursive-div...Recursive division algorithm.')
    print()
    print('Example:')
    print('\tpython maze-generator.py 25 20 dfs')
    print()
'''
if( len(sys.argv) == 1 ) :
    print_error('Invalid syntax, please type the command correctly.')
    exit()

if( (int(sys.argv[1]) < 5 or int(sys.argv[1]) > 30) or (int(sys.argv[2]) < 5 or int(sys.argv[2]) > 30) ) :
    print_error('Invalid dimensions, please enter valid ones.') 
    exit()

if( len(sys.argv) <= 3 ) :
    print_error('Please enter an algorithm.') 
    exit()

if( sys.argv[3] not in algorithms ) :
    print_error('Invalid algorithm, please enter a valid one.') 
    exit()

# GRID WIDTH, HEIGHT AND CELL DIMENSIONS (WIDTH AND HEIGHT)
GRID_W = int(sys.argv[1])
GRID_H = int(sys.argv[2])

if( sys.argv[3] == 'dfs' ) :
    Dfs.generate_maze(GRID_W, GRID_H)
elif( sys.argv[3] == 'prim' ) :
    Prim.generate_maze(GRID_W, GRID_H)
elif( sys.argv[3] == 'kruskal' ) :
    Kruskal.generate_maze(GRID_W, GRID_H)
elif( sys.argv[3] == 'recursive-div' ) :
    RecursiveDivision.generate_maze(GRID_W, GRID_H)
'''

m = maze.Maze(30,30)
m.draw_dfs_algorithm()
#Dfs.generate_maze(5, 5)
