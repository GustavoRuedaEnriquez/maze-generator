import utils.draw as Draw
import algorithms.algorithm_depth_first_search as Dfs
import algorithms.algorithm_prim as Prim
import algorithms.algorithm_kruskal as Kruskal
import algorithms.algorithm_recursive_division as Recursive_Div

class Maze:
  def __init__(self, _width, _height):
    self.width = _width
    self.height = _height
    self.matrix = self.create_blank_maze(_width, _height)

  def __str__(self):
    string = ''
    string += 'W ' + str(self.width) + '\n'
    string += 'H ' + str(self.height) + '\n'
    for i in range(0,len(self.matrix)):
      for j in range(0, len(self.matrix[i])):
        string += ' '
        string += str(self.matrix[i][j])
      string += '\n'
    return string
  
  def write_maze_into_file(self, filename):
    # Custom file must contain maze's important information:
    # - Width
    # - Height
    # - Matrix
    ext = ".maze"
    filepath = filename + ext
    file = open(filepath, "wt")
    file.write(str(self))
    file.close()

  def process_maze_file(self, content):
    content_array = content.split('\n')

    # Remove EOF char (empty string) left
    content_array.remove('')

    # Retrieve width and height
    width_str = content_array[0]
    height_str = content_array[1]

    # Width is saved with the format:
    # W [WIDTH]
    width = int(width_str.split(" ")[1])

    # Height is saved with the format:
    # H [HEIGHT]
    height = int(height_str.split(" ")[1])
    
    # Set maze's dimensions
    self.width = width
    self.height = height

    matrix_str = content_array[2:]
    # First, split each row and remove any blank character
    for i in range(0, len(matrix_str)):
      matrix_str[i] = matrix_str[i].split(' ')
      matrix_str[i].remove('')

    # Now convert string matrix to integer matrix
    matrix = list()
    for i in range(0, len(matrix_str)):
      matrix_row = list()
      for j in range(0, len(matrix_str[i])):
        matrix_row.append(int(matrix_str[i][j]))
      matrix.append(matrix_row)
    
    self.matrix = matrix

  def read_maze_file(self, filename):
    print(filename)
    if (filename.endswith(".maze") == False):
      print("Invalid file extension")
      exit()

    file = open(filename, "rt")
    
    # Retrieve file's content
    content = file.read()
    file.close()

    # Process content
    self.process_maze_file(content)

  def draw_maze(self):
    window, clock = Draw.init_screen("Maze")
    Draw.draw_maze_matrix(window, self.matrix, Draw.COLOR_CYAN)
    Draw.draw_start_end_cells(window, self.matrix, self.width, self.height)
    Draw.run_game_loop(clock)

  def exec_dfs_algorithm(self, create_file, filepath):
    window, clock = Draw.init_screen("Maze generated with DFS algorithm")
    Dfs.generate_maze(window, self.matrix, self.width, self.height)
    if create_file:
      self.write_maze_into_file(filepath)
    Draw.run_game_loop(clock)

  def exec_prim_algorithm(self, create_file, filepath):
    window, clock = Draw.init_screen("Maze generated with Prim's algorithm")
    Prim.generate_maze(window, self.matrix, self.width, self.height)
    if create_file:
      self.write_maze_into_file(filepath)
    Draw.run_game_loop(clock)

  def exec_kruskal_algorithm(self, create_file, filepath):
    window, clock = Draw.init_screen("Maze generated with Kruskal's algorithm")
    Kruskal.generate_maze(window, self.matrix, self.width, self.height)
    if create_file:
      self.write_maze_into_file(filepath)
    Draw.run_game_loop(clock)

  def exec_recursive_division_algorithm(self, create_file, filepath):
    self.matrix = self.create_empty_box(self.width, self.height)
    window, clock = Draw.init_screen("Maze generated with Recursive Division "\
                                     "algorithm")
    Recursive_Div.generate_maze(window, self.matrix, self.width, self.height)
    if create_file:
      self.write_maze_into_file(filepath)
    Draw.run_game_loop(clock)
  
  def create_empty_box(self, _width, _height):
    matrix_cols = (2 * _width) + 1
    slot_value = 0
    maze_matrix = list()
    
    # First row of the matrix must be all walls (0), since it is top's border
    # limit
    maze_wall_row = list()
    for i in range(0, matrix_cols):
      maze_wall_row.append(0)
    maze_matrix.append(maze_wall_row)

    # Since this matrix is only used for recursive division, there are no inner
    # walls here, so the only walls would be located on the first and last cell
    for i in range(0, _height):
      maze_row = list()
      for j in range(0, matrix_cols):
        slot_value = 0 if (j == 0 or j==matrix_cols-1) else 1
        maze_row.append(slot_value)
      maze_matrix.append(maze_row)

    for i in range(0, _height):
      maze_row = list()
      for j in range(0, matrix_cols):
        slot_value = 0 if (j == 0 or j==matrix_cols-1) else 1
        maze_row.append(slot_value)
      maze_matrix.append(maze_row)

    # Last row of the matrix must be all walls (0), since it is bottom's border
    # limit
    maze_wall_row = list()
    for i in range(0, matrix_cols):
      maze_wall_row.append(0)
    maze_matrix.pop()
    maze_matrix.append(maze_wall_row)

    return maze_matrix

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

      maze_row = list()
      for j in range(0, matrix_cols):
        maze_row.append(0)
      maze_matrix.append(maze_row)

    return maze_matrix

    