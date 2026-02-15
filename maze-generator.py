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

program_description = "Tool that allows us to do:\n" \
  "* Create an object representing a maze and display it. Generated following a selected maze generation algorithm.\n" \
  "* Save the maze object on a text file, allowing its future visualization.\n"\
  "* Obtain the route to solve the maze following a selected path-finding algorithm.\n"

parser = argparse.ArgumentParser(
                    prog="maze-generator",
                    description = program_description)

operation = "create-maze"
valid_algorithms = ["dfs", "prim", "kruskal", "recursive-div", "eller"]

# Messages displayed with --help option
size_help  = "total size of the grid, enter it using the following structure:"\
              " widthxheight.Valid values are " \
              "[{} - {}]".format(CELLS_LOW_LIMIT, CELLS_UPPER_LIMIT)
algorithm_help = "desired maze generation algorithm to use. Valid options are "\
                 "[dfs, prim, kruskal, recursive-div, eller]"
write_help = "file name of where the resulting maze will be written"
file_help = "file path of .maze file that is wanted to be drawn"
solve_help = "desired maze solving algorithm to use. Valid options are [a_star]"

parser.add_argument("-sz", "--maze-size", dest="size", help=size_help)
parser.add_argument("-gen", "--generation-algorithm", dest="gen_algorithm", help=algorithm_help)
parser.add_argument("-wrt", "--maze-write", dest="path", help=write_help)
parser.add_argument("-src", "--maze-source", dest="source", help=file_help)
parser.add_argument("-sol", "--solving-algorithm", dest="sol_algorithm", help=solve_help)
args = parser.parse_args()
maze_config = dict()

# Make sure we are not using arguments that conflict each other
if(args.size != None and args.source != None):
  print("Conflicting operations. Nothing to do.")
  exit()

# Check if it is desired to read from an existant *.maze file instead of
# generating a new maze
if (args.source is not None):
  operation = "read-maze"
  maze_config["source"] = args.source

# Check if it is desired to solve the maze after generation
if (args.sol_algorithm is not None):
  maze_config["solving_algorithm"] = args.sol_algorithm

if (operation == "create-maze"):
  # Check size input
  if(args.size is not None):
    size_array = args.size.split('x')
    maze_w = int(size_array[0])
    maze_h = int(size_array[1])
    if (maze_w < CELLS_LOW_LIMIT or maze_w > CELLS_UPPER_LIMIT):
      print ("Width out of range")
      exit()
    elif (maze_h < CELLS_LOW_LIMIT or maze_h > CELLS_UPPER_LIMIT):
      print ("Height out of range")
      exit()
    maze_config["width"] = maze_w
    maze_config["height"] = maze_h

  # Check algorithm input
  if (args.gen_algorithm is not None):
    if (args.gen_algorithm not in valid_algorithms):
      print("Invalid algorithm")
      exit()
    else:
      maze_config["generation_algorithm"] = args.gen_algorithm

  # Check if a file path is passed
  if (args.path is not None):
    maze_config["path"] = args.path

  # Finally, generate the maze
  m = maze.Maze(maze_config)
  m.generate()

elif (operation == "read-maze"):
  m = maze.Maze(maze_config)
  m.draw_maze()
