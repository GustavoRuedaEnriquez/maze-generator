# pylint: disable=no-member

import sys
import depth_first_search as Dfs

if( len(sys.argv) == 1 ) :
    print()
    print('Invalid syntax, please type the command correctly.') 
    print('Usage:') 
    print('\tpython maze-generator.py [WIDTH] [HEIGHT]')
    print('\tWIDTH  - The number of cells alongside the width.  The valid values are [5 - 30]')
    print('\tHEIGHT - The number of cells alongside the height. The valid values are [5 - 30]')
    print()
    print('Example:')
    print('\tpython maze-generator.py 25 20')
    print()
    exit()

if( (int(sys.argv[1]) < 5 or int(sys.argv[1]) > 30) or (int(sys.argv[2]) < 5 or int(sys.argv[2]) > 30) ) :
    print()
    print('Invalid dimensions, please enter valid ones.') 
    print('Usage:') 
    print('\tpython maze-generator.py [WIDTH] [HEIGHT]')
    print('\tWIDTH  - The number of cells alongside the width.  The valid values are [5 - 30]')
    print('\tHEIGHT - The number of cells alongside the height. The valid values are [5 - 30]')
    print()
    print('Example:')
    print('\tpython maze-generator.py 25 20')
    print()
    exit()

# GRID WIDTH, HEIGHT AND CELL DIMENSIONS (WIDTH AND HEIGHT)
GRID_W = int(sys.argv[1])
GRID_H = int(sys.argv[2])

Dfs.generate_maze(GRID_W, GRID_H)