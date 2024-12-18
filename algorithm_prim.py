"""
--------------------------------
| Maze-Generator               |
| Prim's algorithm             |
-------------------------------
Author: Gustavo Adolfo Rueda Enríquez
Python 3.8

"""
import time
import random
import utils.draw as Draw

#CELLS DIMENSION (WIDTH AND HEIGHT)
CELL_D = Draw.getCellWidth()

# CELLS ARRAY
maze = []
frontiers = []

def trace_maze_prim(Window, Grid, Grid_width, Grid_height, Size) :
    # Choose random value
    start = random.choice(Grid)
    x = start[0]
    y = start[1]
    maze.append(start)
    Draw.draw_cell(Window,x, y, Draw.COLOR_BLUE)
    
    # Search for the possible frontiers.
    if( ((x, y - Size) not in frontiers) and ((x, y - Size) in Grid) ) :
        frontiers.append((x, y - Size))
        Draw.draw_cell(Window, x, y - Size, Draw.COLOR_GREEN)
    if( ((x - Size, y) not in frontiers) and ((x - Size, y) in Grid) ) :
        frontiers.append((x - Size, y))
        Draw.draw_cell(Window, x - Size, y, Draw.COLOR_GREEN)
    if( ((x, y + Size) not in frontiers) and ((x, y + Size) in Grid) ) :
        frontiers.append((x, y + Size))
        Draw.draw_cell(Window, x, y + Size, Draw.COLOR_GREEN)
    if( ((x + Size, y) not in frontiers) and ((x + Size, y) in Grid) ) :
        frontiers.append((x + Size, y))
        Draw.draw_cell(Window, x + Size, y, Draw.COLOR_GREEN)

    while(len(frontiers) > 0) :
        # Sleep for a little bit
        time.sleep(0.01)

        # Obtain a random frontier cell
        frontier = frontiers.pop(random.randrange(len(frontiers)))
        x = frontier[0]
        y = frontier[1]
        neighbors = []

        # Search for the possible neighbors.
        if( ((x, y - Size) in maze) and ((x, y - Size) in Grid) ) :
            neighbors.append('top')
        if( ((x - Size, y) in maze) and ((x - Size, y) in Grid) ) :
            neighbors.append('left')
        if( ((x, y + Size) in maze) and ((x, y + Size) in Grid) ) :
            neighbors.append('bottom')
        if( ((x + Size, y) in maze) and ((x + Size, y) in Grid) ) :
            neighbors.append('right')
        
        # Check which neighbor to merge
        if(len(neighbors) > 0) :
            neighbor = random.choice(neighbors)
            if(neighbor == 'top') :
                Draw.draw_next_cell(Window, x, y, 'up', Draw.COLOR_BLUE)
                maze.append((x, y))
            elif(neighbor == 'left') :
                Draw.draw_next_cell(Window, x, y, 'left', Draw.COLOR_BLUE)
                maze.append((x, y))
            elif(neighbor == 'bottom') :
                Draw.draw_next_cell(Window, x, y, 'down', Draw.COLOR_BLUE)
                maze.append((x, y))
            elif(neighbor == 'right') :
                Draw.draw_next_cell(Window, x, y, 'right', Draw.COLOR_BLUE)
                maze.append((x, y))

        # Search and add the possible frontiers.
            if( ((x, y - Size) not in frontiers) and ((x, y - Size) in Grid) and ((x, y - Size) not in maze) ) :
                frontiers.append((x, y - Size))
                Draw.draw_cell(Window, x, y - Size, Draw.COLOR_GREEN)
            if( ((x - Size, y) not in frontiers) and ((x - Size, y) in Grid) and ((x - Size, y) not in maze) ) :
                frontiers.append((x - Size, y))
                Draw.draw_cell(Window, x - Size, y, Draw.COLOR_GREEN)
            if( ((x, y + Size) not in frontiers) and ((x, y + Size) in Grid) and ((x, y + Size) not in maze) ) :
                frontiers.append((x, y + Size))
                Draw.draw_cell(Window, x, y + Size, Draw.COLOR_GREEN)
            if( ((x + Size, y) not in frontiers) and ((x + Size, y) in Grid) and ((x + Size, y) not in maze) ) :
                frontiers.append((x + Size, y))
                Draw.draw_cell(Window, x + Size, y, Draw.COLOR_GREEN)

    Draw.draw_fill_start_and_end_cells(Window, Grid_width, Grid_height)
            
def generate_maze(Width, Height) :
    window, clock = Draw.init_screen('Maze generated with Prim\'s algorithm.')
    grid = Draw.draw_grid (window, Width, Height)
    trace_maze_prim(window, grid, Width, Height, CELL_D)
    Draw.run_game_loop(clock)