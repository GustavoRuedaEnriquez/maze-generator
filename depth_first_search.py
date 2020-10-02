import random
import utils.draw as Draw

CELL_D = 20

# CELLS ARRAY
stack   = []
visited = []

def trace_maze_dfs(Window, Grid, X, Y, W) :
    Draw.draw_current_cell(Window, X, Y)
    stack.append((X, Y))
    visited.append((X, Y))

    while(len(stack) > 0) :
        # Check which neighbours are available
        available_cells = []
        if( ((X, Y - W) not in visited) and ((X, Y - W) in Grid) ) :
            available_cells.append('top')
        if( ((X - W, Y) not in visited) and ((X - W, Y) in Grid) ) :
            available_cells.append('left')
        if( ((X, Y + W) not in visited) and ((X, Y + W) in Grid) ) :
            available_cells.append('bottom')
        if( ((X + W, Y) not in visited) and ((X + W, Y) in Grid) ) :
            available_cells.append('right')
        # Select a random neighbour
        if(len(available_cells) != 0) :
            next_cell = random.choice(available_cells)
            if(next_cell == 'top') :
                Draw.draw_next_cell(Window, X, Y, W, 'up')
                visited.append((X, Y - W))
                stack.append((X, Y - W))
                Y = Y - W
            elif(next_cell == 'left') :
                Draw.draw_next_cell(Window, X, Y, W, 'left')
                visited.append((X - W, Y))
                stack.append((X - W, Y))
                X = X - W
            elif(next_cell == 'bottom') :
                Draw.draw_next_cell(Window, X, Y, W, 'down')
                visited.append((X, Y + W))
                stack.append((X, Y + W))
                Y = Y + W
            elif(next_cell == 'right') :
                Draw.draw_next_cell(Window, X, Y, W, 'right')
                visited.append((X + W, Y))
                stack.append((X + W, Y))
                X = X + W
        else :
            X, Y = stack.pop()
            Draw.draw_current_cell(Window, X, Y)
            Draw.draw_backtracking_cell(Window, X, Y)

def generate_maze(Width, Height) :
    window, clock = Draw.init_screen('Maze generated with depth first search algorithm.')
    grid = Draw.draw_grid (window, 0, 0, CELL_D, Width, Height)
    trace_maze_dfs(window, grid, CELL_D, CELL_D, CELL_D)
    Draw.run_game_loop(clock)
