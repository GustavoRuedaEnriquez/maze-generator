# pylint: disable=no-member

"""
--------------------------------
| Maze-Generator               |
| Main program                 |
-------------------------------
Author: Gustavo Adolfo Rueda Enríquez
Python 3.8

"""

import argparse
import maze

CELLS_LOW_LIMIT = 5
CELLS_UPPER_LIMIT = 40

program_description = "Tool that allows us to do 2 main actions: create custom"\
  " random mazes using a specified algorithm  and draw it on screen; or draw a"\
  " maze based on a existing maze file.\n"

parser = argparse.ArgumentParser(
                    prog="maze-generator",
                    description = program_description)

maze_w = 5
maze_h = 5
maze_algorithm = "dfs"
algorithms = ['dfs', 'prim']#, 'kruskal', 'recursive-div']

# Messages displayed with --help option
size_help  = "total size of the grid, enter it using the following structure:"\
              " widthxheight.Valid values are " \
              "[{} - {}]".format(CELLS_LOW_LIMIT, CELLS_UPPER_LIMIT)
algorithm_help = "desired maze generation algorithm to use. Valid options are "\
                 "[dfs, prim, kruskal, recursive-div]"
write_help = "file name of where the resulting maze will be written"
file_help = "file path of .maze file that is wanted to be drawn"


parser.add_argument("-s", "--size", dest="size", help=size_help, default="5x5")
parser.add_argument("-a", "--algorithm", dest="algorithm", default="dfs", \
                    help=algorithm_help)
parser.add_argument("-wr", "--write", dest="filepath", help=write_help)
parser.add_argument("-f", "--file", dest="filesource", help=file_help)
args = parser.parse_args()

# Make sure we are not using arguments that conflict each other
if(args.size != None and args.filesource != None):
  print("Conflicting operations. Nothing done.")
  exit()

# OPTION 1: Create a custom maze.

# Check size input
if(args.size != None):
  size_array = args.size.split('x')
  maze_w = int(size_array[0])
  maze_h = int(size_array[1])
  if (maze_w < CELLS_LOW_LIMIT or maze_w > CELLS_UPPER_LIMIT):
    print ("Width out of range")
    exit()
  if (maze_h < CELLS_LOW_LIMIT or maze_h > CELLS_UPPER_LIMIT):
    print ("Height out of range")
    exit()

# Check algorithm input
if (args.algorithm != None):
  if (args.algorithm not in algorithms):
    print("Invalid algorithm")
    exit()
  else:
    maze_algorithm = args.algorithm


# Finally, build the maze
m = maze.Maze(maze_w, maze_h)

if( maze_algorithm == 'dfs' ) :
    m.draw_dfs_algorithm()
elif( maze_algorithm == 'prim' ) :
    m.draw_prim_algorithm()



m.draw_dfs_algorithm()
#m.draw_prim_algorithm()'''