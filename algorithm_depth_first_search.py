"""
--------------------------------
| Maze-Generator               |
| Depth first search algorithm |
-------------------------------
Author: Gustavo Adolfo Rueda Enríquez
Python 3.8

"""

import random
import utils.draw as Draw

#CELLS DIMENSION
CELL_D = Draw.getCellWidth()

# CELLS ARRAY
stack   = []
visited = []

def has_neighbors(Grid, Position) :
    X = Position[0]
    Y = Position[1]
    top = ((X, Y - CELL_D) not in visited) and ((X, Y - CELL_D) in Grid)
    left = ((X - CELL_D, Y) not in visited) and ((X - CELL_D, Y) in Grid)
    bottom = ((X, Y + CELL_D) not in visited) and ((X, Y + CELL_D) in Grid)
    right = ((X + CELL_D, Y) not in visited) and ((X + CELL_D, Y) in Grid)
    return top or left or bottom or right

def get_neighbors(Grid, Position) :
    X = Position[0]
    Y = Position[1]
    available_neighbors = []
    if( ((X, Y - CELL_D) not in visited) and ((X, Y - CELL_D) in Grid) ) :
        available_neighbors.append('top')
    if( ((X - CELL_D, Y) not in visited) and ((X - CELL_D, Y) in Grid) ) :
        available_neighbors.append('left')
    if( ((X, Y + CELL_D) not in visited) and ((X, Y + CELL_D) in Grid) ) :
        available_neighbors.append('bottom')
    if( ((X + CELL_D, Y) not in visited) and ((X + CELL_D, Y) in Grid) ) :
        available_neighbors.append('right')
    return available_neighbors

def trace_maze_dfs(Window, Grid, Grid_width, Grid_height, X, Y, Size) :
    Draw.draw_cell(Window, X, Y, Draw.COLOR_GREEN)
    stack.append((X, Y))
    visited.append((X, Y))

    while(len(stack) > 0) :
        # Check which neighbors are available.
        available_cells = get_neighbors(Grid, (X, Y))
            
        # Select a random neighbor and move the cell to it.
        if(len(available_cells) != 0) :
            next_cell = random.choice(available_cells)
            if(next_cell == 'top') :
                Draw.draw_next_cell(Window, X, Y, 'up', Draw.COLOR_VIOLET)
                visited.append((X, Y - Size))
                stack.append((X, Y - Size))
                Y = Y - Size
            elif(next_cell == 'left') :
                Draw.draw_next_cell(Window, X, Y, 'left', Draw.COLOR_VIOLET)
                visited.append((X - Size, Y))
                stack.append((X - Size, Y))
                X = X - Size
            elif(next_cell == 'bottom') :
                Draw.draw_next_cell(Window, X, Y, 'down', Draw.COLOR_VIOLET)
                visited.append((X, Y + Size))
                stack.append((X, Y + Size))
                Y = Y + Size
            elif(next_cell == 'right') :
                Draw.draw_next_cell(Window, X, Y, 'right', Draw.COLOR_VIOLET)
                visited.append((X + Size, Y))
                stack.append((X + Size, Y))
                X = X + Size

            # Mark the new current cell's position
            Draw.draw_cell(Window, X, Y, Draw.COLOR_GREEN)
        else :
            # Mark current cell as part of the maze
            Draw.draw_cell(Window, X, Y, Draw.COLOR_BLUE)
            
            # Redraw the backtracked path, peeking if the previous element had neighbors,
            # if it does not have any neighbors, marked as part of the maze. Continue with
            # the neighbors otherwise.
            old_x, old_y = X, Y
            if(has_neighbors(Grid, stack[-1]) != True) :
                X, Y = stack.pop()
                if(old_x > X) :
                    Draw.draw_next_cell(Window, X, Y, 'right', Draw.COLOR_BLUE)
                elif(old_x < X) :
                    Draw.draw_next_cell(Window, X, Y, 'left', Draw.COLOR_BLUE)
                elif(old_y > Y) :
                    Draw.draw_next_cell(Window, X, Y, 'down', Draw.COLOR_BLUE)
                elif(old_y < Y) :
                    Draw.draw_next_cell(Window, X, Y, 'up', Draw.COLOR_BLUE)
            else :
                X, Y = stack[-1][0], stack[-1][1]
                if(old_x > X) :
                    Draw.draw_next_cell_line(Window, X, Y, 'right', Draw.COLOR_BLUE)
                elif(old_x < X) :
                    Draw.draw_next_cell_line(Window, X, Y, 'left', Draw.COLOR_BLUE)
                elif(old_y > Y) :
                    Draw.draw_next_cell_line(Window, X, Y, 'down', Draw.COLOR_BLUE)
                elif(old_y < Y) :
                    Draw.draw_next_cell_line(Window, X, Y, 'up', Draw.COLOR_BLUE)
                
    # Draw the start and the end
    Draw.draw_cell(Window, Size, Size, Draw.COLOR_RED)
    Draw.draw_cell(Window, Grid_width * Size, Grid_height * Size, Draw.COLOR_RED)

def generate_maze(Width, Height) :
    window, clock = Draw.init_screen('Maze generated with depth first search algorithm.')
    grid = Draw.draw_grid (window, Width, Height)
    trace_maze_dfs(window, grid, Width, Height, CELL_D, CELL_D, CELL_D)
    Draw.run_game_loop(clock)