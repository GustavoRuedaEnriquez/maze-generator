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
generation_algorithm = "dfs"
create_file = False
filepath = ""
filesource = ""
operation = "create-maze"
solve_maze = False
solving_algorithm = "a_star"

algorithms = ["dfs", "prim", "kruskal", "recursive-div", "eller"]

# Messages displayed with --help option
size_help  = "total size of the grid, enter it using the following structure:"\
              " widthxheight.Valid values are " \
              "[{} - {}]".format(CELLS_LOW_LIMIT, CELLS_UPPER_LIMIT)
algorithm_help = "desired maze generation algorithm to use. Valid options are "\
                 "[dfs, prim, kruskal, recursive-div, eller]"
write_help = "file name of where the resulting maze will be written"
file_help = "file path of .maze file that is wanted to be drawn"
solve_help = "desired maze solving algorithm to use. Valid options are [a_star]"

parser.add_argument("-s", "--size", dest="size", help=size_help)
parser.add_argument("-a", "--algorithm", dest="algorithm", help=algorithm_help)
parser.add_argument("-wr", "--write", dest="filepath", help=write_help)
parser.add_argument("-r", "--read", dest="filesource", help=file_help)
parser.add_argument("-so", "--solve", dest="solve", help=solve_help)
args = parser.parse_args()
maze_config = dict()

# Make sure we are not using arguments that conflict each other
if(args.size != None and args.filesource != None):
  print("Conflicting operations. Nothing done.")
  exit()

if (args.filesource != None):
  operation = "read-maze"
  maze_config["source"] = args.filesource

if (operation == "create-maze"):

  # Check size input
  if(args.size != None):
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
  if (args.algorithm is not None):
    if (args.algorithm not in algorithms):
      print("Invalid algorithm")
      exit()
    else:
      maze_config["generation_algorithm"] = args.algorithm

  # Check if a file path is passed
  if (args.filepath is not None):
    maze_config["path"] = args.filepath

  # Check if it is desired to solve the maze after generation
  if (args.solve is not None):
    maze_config["solving_algorithm"] = args.solve

  # Finally, generate the maze
  m = maze.Maze(maze_config)
  m.generate()


"""elif (operation == "read-maze"):
  m = maze.Maze(CELLS_LOW_LIMIT, CELLS_LOW_LIMIT)
  m.read_maze_file(filesource)
  m.draw_maze()"""
