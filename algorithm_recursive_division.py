"""
--------------------------------
| Maze-Generator               |
| Recursive Division algorithm |
-------------------------------
Author: Gustavo Adolfo Rueda Enríquez
Python 3.8

"""

import random
import utils.draw as Draw

#BISECT DIRECTIONS
VERTICAL, HORIZONTAL = 0,1

def bisect_maze(Window, sx, sy, ex, ey) :
    # Calculate our free work area
    dx = ex - sx
    dy = ey - sy
    # Stop condition
    if dx <= 1 or dy <= 1:
        return
    # Choose wall direction
    if dy > dx:
        direction = HORIZONTAL
    elif dx >= dy:
        direction = VERTICAL
    # Select the bisection point
    while True :
        px = random.randrange(sx, ex)
        py = random.randrange(sy, ey)
        if(px > sx and px < ex and py > sy and py < ey ) :
            break
    # Draw line
    Draw.draw_bisect_grid(Window, sx , sy, ex, ey, direction, px, py)
    # Draw hallway
    Draw.draw_gap_grid(Window, sx, sy, ex, ey, direction, px, py)
    # Prepare for next iteration
    if direction == HORIZONTAL:
        bisect_maze(Window, sx, sy, ex, py)
        bisect_maze(Window, sx, py, ex, ey)
    else :
        bisect_maze(Window, sx, sy, px, ey)
        bisect_maze(Window, px, sy, ex, ey)

def trace_maze_recursive_division(Window, Width, Height) :
    bisect_maze(Window, 0, 0, Width, Height)
    Draw.draw_fill_start_and_end_cells(Window, Width, Height)

def generate_maze(Width, Height) :
    window, clock = Draw.init_screen('Maze generated with recursive division algorithm.')
    Draw.draw_grid_outer_line (window, Width, Height)
    Draw.draw_fill_grid_color(window, Draw.COLOR_BLUE, Width, Height)
    trace_maze_recursive_division(window, Width, Height)
    Draw.run_game_loop(clock)