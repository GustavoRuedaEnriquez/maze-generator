"""
------------------
| Maze-Generator |
| A* algorithm   |
------------------
Author: Gustavo Adolfo Rueda Enriquez
Python 3.8
"""
import time
import utils.draw as Draw
from queue import PriorityQueue

SLOT_NOT_USABLE_CONST = 0
SLOT_USABLE_CONST = 1

NODE_STATE_UNEXPLORED = 0
NODE_STATE_OPEN = 1
NODE_STATE_CLOSED = 2

class MazeNode:
  def __init__(self, _pos, _value):
    self.pos = _pos
    self.state = NODE_STATE_UNEXPLORED
    self.value = _value
    self.neighbors = list()

  def __lt__(self, _other):
    return False

  def __str__(self):
    string = "MazeNode pos" + str(self.pos) + ' Neighbors=['
    count = 0
    for n in self.neighbors:
      string += str(n.get_pos())
      if count < len(self.neighbors) - 1:
        string += ', '
      count += 1
    string += ']'
    return string

  def get_pos(self):
    return self.pos

  def get_state(self):
    return self.state

  def get_value(self):
    return self.value
  
  def get_neighbors(self):
    return self.neighbors
  
  def set_state(self, _state):
    self.state = _state

  def is_closed(self):
    return self.state == NODE_STATE_CLOSED
  
  def update_neighbors(self, matrix):
    row = self.get_pos()[0]
    col = self.get_pos()[1]

    # Check cell on the left
    if col - 1 >= 0 and matrix[row][col - 1].get_value() is SLOT_USABLE_CONST:
     self.neighbors.append(matrix[row][col - 1])
    # Check cell on the right
    if col + 1 < len(matrix[row]) and matrix[row][col + 1].get_value()  is SLOT_USABLE_CONST:
      self.neighbors.append(matrix[row][col + 1])
    # Check cell from above
    if row - 1 >= 0 and matrix[row - 1][col].get_value() is SLOT_USABLE_CONST:
      self.neighbors.append(matrix[row - 1][col])
    # Check cell from below
    if row + 1 < len(matrix) and matrix[row + 1][col].get_value() is SLOT_USABLE_CONST:
      self.neighbors.append(matrix[row + 1][col])

def reconstruct_path(window, maze_matrix, origin_node, current_node):
  while current_node in origin_node:
    Draw.draw_cell(window, maze_matrix, current_node.get_pos(), Draw.COLOR_CYAN)
    current_node = origin_node[current_node]

def execute_a_star_algorithm(window, maze_matrix, graph, start, goal):
  count = 0
  # Scores and fields required
  g_score = {node: float("inf") for node in graph}
  f_score = {node: float("inf") for node in graph}
  origin_node = {}
  open_nodes_pqueue = PriorityQueue()
  open_nodes_set = set()
  
  # Initialize all fields/scores
  g_score[start] = 0
  f_score[start] = heuristic_func(start, goal)
  open_nodes_pqueue.put((0, count, start))
  open_nodes_set.add(start)

  # The algorithm will run until the priority queue is empty
  while not open_nodes_pqueue.empty():
    current_node = open_nodes_pqueue.get()[2]
    open_nodes_set.remove(current_node)

    if current_node is goal:
      # Reconstruct the path
      reconstruct_path(window, maze_matrix, origin_node, current_node)
      return True

    for neighbor in current_node.get_neighbors():
      temp_g_score = g_score[current_node] + 1
      if temp_g_score < g_score[neighbor]:
        origin_node[neighbor] = current_node
        g_score[neighbor] = temp_g_score
        f_score[neighbor] = temp_g_score + heuristic_func(neighbor, goal)
        if neighbor not in open_nodes_set:
          count += 1
          open_nodes_pqueue.put((f_score, count, neighbor))
          open_nodes_set.add(neighbor)
          neighbor.set_state(NODE_STATE_OPEN)
          Draw.draw_cell(window, maze_matrix, neighbor.get_pos(), Draw.COLOR_GREEN)
  
    if current_node is not start:
      current_node.set_state(NODE_STATE_CLOSED)
      Draw.draw_cell(window, maze_matrix, current_node.get_pos(), Draw.COLOR_ORANGE)
      
  return

def solve_maze(window, config):
  matrix = config["maze_matrix"]
  width = config["width"]
  height = config["height"]
  maze_nodes_matrix, start, goal = parse_int_matrix(matrix, width, height)
  traversable_nodes = get_traversable_nodes(maze_nodes_matrix)
  execute_a_star_algorithm(window, maze_nodes_matrix, traversable_nodes, start, goal)
  Draw.draw_start_end_cells(window, matrix, width, height)

def get_traversable_nodes(matrix):
  traversable_nodes = list()
  rows = len(matrix)

  # Check which nodes are usuable
  for i in range(0, rows):
    cols = len(matrix[i])
    for j in range(0, cols):
      node = matrix[i][j]
      if node.get_value() is SLOT_USABLE_CONST:
        traversable_nodes.append(node)

  return traversable_nodes

def parse_int_matrix(matrix, width, height):
  maze_nodes_matrix = list()
  rows = len(matrix)
  start_node = None
  goal_node = None

  # Create a matrix of MazeNode objects
  for i in range(0, rows):
    cols = len(matrix[i])
    maze_nodes_row = list()
    for j in range(0, cols):
      node = MazeNode((i, j), matrix[i][j])
      # Maze's start is ALWAYS at [1,1]
      if i == 1 and j == 1:
        start_node = node
      # Maze's goal is ALWAYS on the last usable slot on last row, last column.
      elif i == (2 * height) - 1 and j == (2 * width) - 1:
        goal_node = node
      maze_nodes_row.append(node)
    maze_nodes_matrix.append(maze_nodes_row)

  # Populate neighbors of each traversable node
  traversable_nodes = get_traversable_nodes(maze_nodes_matrix)
  for node in traversable_nodes:
    node.update_neighbors(maze_nodes_matrix)

  return maze_nodes_matrix, start_node, goal_node

# Manhattan distance
def heuristic_func(node_1, node_2):
  row_1, col_1 = node_1.get_pos()
  row_2, col_2 = node_2.get_pos()
  return abs(row_1 - row_2) + abs(col_1 - col_2)
