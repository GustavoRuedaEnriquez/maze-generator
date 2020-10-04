import random
import utils.draw as Draw

#CELLS DIMENSION (WIDTH AND HEIGHT)
CELL_D = 20

# CELLS ARRAY
trees = []

def trace_maze_kruskal(Window, Grid, Grid_width, Grid_height, Size) :
    print('TODO')

def generate_maze(Width, Height) :
    window, clock = Draw.init_screen('Maze generated with Kruskal\'s algorithm.')
    grid = Draw.draw_grid (window, 0, 0, CELL_D, Width, Height)
    trace_maze_kruskal(window, grid, Width, Height, CELL_D)
    Draw.run_game_loop(clock)

generate_maze(30, 30)