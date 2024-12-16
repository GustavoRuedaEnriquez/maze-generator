import utils.draw as Draw
import algorithm_depth_first_search as Dfs
import time
class Maze:
  def __init__(self, _width, _height):
    self.width = _width
    self.height = _height
    self.matrix = self.create_blank_maze(_width, _height)

  def __str__(self):
    string = ''
    for i in range(0,len(self.matrix)):
      for j in range(0, len(self.matrix[i])):
        string += ' '
        string += str(self.matrix[i][j])
      string += '\n'
    return string

  def draw_matrix(self):
    window, clock = Draw.init_screen('Maze')
    Draw.draw_maze_matrix(window, self.matrix)
    Draw.run_game_loop(clock)

  def draw_dfs_algorithm(self):
    window, clock = Draw.init_screen('Maze generated with DFS algorithm')
    Dfs.generate_maze(window, clock, self.matrix, self.width, self.height)


  def create_blank_maze(self, _width, _height):
    matrix_cols = (2 * _width) + 1
    slot_value = 0
    maze_matrix = list()
    
    # First row of the matrix must be all walls (0), since it is top´s border
    # limit
    maze_wall_row = list()
    for i in range(0, matrix_cols):
      maze_wall_row.append(0)
    maze_matrix.append(maze_wall_row)

    # For each row, we alternate between walls (0) and free slots (1). We also
    # add a wall row after the alternated row.
    for i in range(0, _height):
      maze_row = list()
      for j in range(0, matrix_cols):
        slot_value = j % 2
        maze_row.append(slot_value)
      maze_matrix.append(maze_row)
      maze_matrix.append(maze_wall_row)

    return maze_matrix

    