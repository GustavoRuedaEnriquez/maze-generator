"""
--------------------------------
| Maze-Generator               |
| Kruskal's algorithm          |
-------------------------------
Author: Gustavo Adolfo Rueda Enríquez
Python 3.8

"""

import time
import copy
import random
import utils.draw as Draw

#CELLS DIMENSION (WIDTH AND HEIGHT)
CELL_D = Draw.getCellWidth()

# CELLS ARRAY
edges = []

def create_set(Grid) :
    sets = []
    for coordinate in Grid :
        x, y = coordinate[0], coordinate[1]
        temp = set()
        temp.add((x,y))
        sets.append( temp )
    return sets

def on_same_set(Position_1, Position_2, Sets) :
    x1 = Position_1[0]
    y1 = Position_1[1]
    x2 = Position_2[0]
    y2 = Position_2[1]

    # Check if a position 1 is on the same set as position 2
    for Set in Sets :
        if( (x1, y1) in Set ) and ( (x2, y2) in Set ) :  
            return True
    return False

def merge_sets(Position_1, Position_2, Sets) :
    i1 = 0
    i2 = 0
    set_1 = set()
    set_2 = set()

    # Get the position 1 set 
    for Set in Sets :
        if( (Position_1[0], Position_1[1]) in Set ) :  
            set_1 = copy.deepcopy(Set)
            break
        i1 = i1 + 1
    # Get the position 2 set 
    for Set in Sets :
        if( (Position_2[0], Position_2[1]) in Set ) :  
            set_2 = copy.deepcopy(Set)
            break
        i2 = i2 + 1

    # Remove the 2 sets
    Sets.pop(i1)

    if(i1 < i2) :
        Sets.pop(i2 - 1)
    else :
        Sets.pop(i2)

    # Create and add the new merged set
    new_set = set()
    new_set = new_set.union(set_1)
    new_set = new_set.union(set_2)

    Sets.append(new_set)


def obtain_unconnected_neighbor(Grid, Sets, X, Y) :
    candidates = []
    
    if( (X, Y - CELL_D) in Grid ) :
        if( on_same_set((X, Y), (X, Y - CELL_D), Sets) == False ) :
            candidates.append('top')
    if( (X - CELL_D, Y) in Grid ) :
        if( on_same_set((X, Y), (X - CELL_D, Y), Sets) == False ) :
            candidates.append('left')
    if( (X, Y + CELL_D) in Grid ) :
        if( on_same_set((X, Y), (X, Y + CELL_D), Sets) == False ) :
            candidates.append('bottom')
    if( (X + CELL_D, Y) in Grid ) :
        if( on_same_set((X, Y), (X + CELL_D, Y), Sets) == False ) :
            candidates.append('right')
    
    if(len(candidates) == 0) :
        neighbor = None
    else :
        neighbor = random.choice(candidates)
        if( neighbor == 'top') :
            merge_sets((X, Y), (X, Y - CELL_D), Sets)
        elif( neighbor == 'left') :
            merge_sets((X, Y), (X - CELL_D, Y), Sets)
        elif( neighbor == 'bottom') :
            merge_sets((X, Y), (X, Y + CELL_D), Sets)
        elif( neighbor == 'right') :
            merge_sets((X, Y), (X + CELL_D, Y), Sets)
    return neighbor

def trace_maze_kruskal(Window, Grid, Grid_width, Grid_height, Size) :
    sets = create_set(Grid)
    edges = copy.deepcopy(Grid)
    random.shuffle(edges)
    index = 0
    total_sets = len(sets)

    while(len(sets) > 1) :
        # Sleep for a little bit
        time.sleep(0.01)
        
        x, y = edges[index]
        neighbor = obtain_unconnected_neighbor(Grid, sets, x, y)
        if( neighbor != None ) :
            if(neighbor == 'top') :
                Draw.draw_next_cell(Window, x, y, 'up', Draw.COLOR_BLUE)
            elif(neighbor == 'left') :
                Draw.draw_next_cell(Window, x, y, 'left', Draw.COLOR_BLUE)
            elif(neighbor == 'bottom') :
                Draw.draw_next_cell(Window, x, y, 'down', Draw.COLOR_BLUE)
            elif(neighbor == 'right') :
                Draw.draw_next_cell(Window, x, y, 'right', Draw.COLOR_BLUE)
        index = (index + 1) % total_sets
    
    Draw.draw_fill_start_and_end_cells(Window, Grid_width, Grid_height)

def generate_maze(Width, Height) :
    window, clock = Draw.init_screen('Maze generated with Kruskal\'s algorithm.')
    grid = Draw.draw_grid (window, Width, Height)
    trace_maze_kruskal(window, grid, Width, Height, CELL_D)
    Draw.run_game_loop(clock)