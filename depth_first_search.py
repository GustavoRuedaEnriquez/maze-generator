import random
import utils.draw as Draw

#CELLS DIMENSION (WIDTH AND HEIGHT)
CELL_D = 20

# CELLS ARRAY
stack   = []
visited = []

def trace_maze_dfs(Window, Grid, Grid_width, Grid_height, X, Y, Size) :
    Draw.draw_current_cell(Window, X, Y)
    stack.append((X, Y))
    visited.append((X, Y))

    while(len(stack) > 0) :
        # Check which neighbours are available
        available_cells = []
        if( ((X, Y - Size) not in visited) and ((X, Y - Size) in Grid) ) :
            available_cells.append('top')
        if( ((X - Size, Y) not in visited) and ((X - Size, Y) in Grid) ) :
            available_cells.append('left')
        if( ((X, Y + Size) not in visited) and ((X, Y + Size) in Grid) ) :
            available_cells.append('bottom')
        if( ((X + Size, Y) not in visited) and ((X + Size, Y) in Grid) ) :
            available_cells.append('right')
        # Select a random neighbour
        if(len(available_cells) != 0) :
            next_cell = random.choice(available_cells)
            if(next_cell == 'top') :
                Draw.draw_next_cell(Window, X, Y, Size, 'up')
                visited.append((X, Y - Size))
                stack.append((X, Y - Size))
                Y = Y - Size
            elif(next_cell == 'left') :
                Draw.draw_next_cell(Window, X, Y, Size, 'left')
                visited.append((X - Size, Y))
                stack.append((X - Size, Y))
                X = X - Size
            elif(next_cell == 'bottom') :
                Draw.draw_next_cell(Window, X, Y, Size, 'down')
                visited.append((X, Y + Size))
                stack.append((X, Y + Size))
                Y = Y + Size
            elif(next_cell == 'right') :
                Draw.draw_next_cell(Window, X, Y, Size, 'right')
                visited.append((X + Size, Y))
                stack.append((X + Size, Y))
                X = X + Size
        else :
            X, Y = stack.pop()
            Draw.draw_current_cell(Window, X, Y)
            Draw.draw_backtracking_cell(Window, X, Y)
    Draw.draw_cell(Window, Size, Size, Draw.COLOR_RED)
    Draw.draw_cell(Window, Grid_width * Size, Grid_height * Size, Draw.COLOR_RED)

def generate_maze(Width, Height) :
    window, clock = Draw.init_screen('Maze generated with depth first search algorithm.')
    grid = Draw.draw_grid (window, 0, 0, CELL_D, Width, Height)
    trace_maze_dfs(window, grid, Width, Height, CELL_D, CELL_D, CELL_D)
    Draw.run_game_loop(clock)