# pylint: disable=no-member
# pylint: disable=unused-variable

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
os.environ['SDL_VIDEO_CENTERED'] = "True"

import time
import pygame


# GUI WINDOW DIMENSIONS
SCREEN_W = 650
SCREEN_H = 650

# FRAMES
FPS = 30

# COLORS DEFINITIONS
COLOR_WHITE  = (255, 255, 255)
COLOR_BLACK  = (0, 0, 0)
COLOR_RED    = (255, 0, 0)
COLOR_GREEN  = (0, 255, 0)
COLOR_BLUE   = (0, 0, 255)
COLOR_VIOLET = (153, 51, 153)

def init_screen(Title) :
    pygame.init()
    pygame.mixer.init()
    window = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption(Title)
    clock = pygame.time.Clock()
    return window, clock

def run_game_loop(Clock) :
    while True:
        Clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

def draw_grid (Window, X, Y, W, Rows, Columns) :
    grid = []
    for i in range(0, Columns):
        X = W
        Y = Y + W
        for j in range(0, Rows):
            # Top cell margin
            pygame.draw.line(Window, COLOR_WHITE, [X, Y], [X + W, Y])
            # Left cell margin
            pygame.draw.line(Window, COLOR_WHITE, [X, Y], [X, Y + W])
            # Bottom cell margin
            pygame.draw.line(Window, COLOR_WHITE, [X, Y + W], [X + W, Y + W])
            # Right cell margin
            pygame.draw.line(Window, COLOR_WHITE, [X + W, Y], [X + W, Y + W])
            grid.append((X, Y))
            X = X + W
        pygame.display.update()
    return grid

def draw_cell(Window, X, Y, Color) :
    pygame.draw.rect(Window, Color, (X + 1, Y + 1, 19, 19), 0)
    pygame.display.update()

def draw_next_cell(Window, X, Y, W, Direction, Color) :
    # Go to the top cell
    if(Direction == 'up') :
        pygame.draw.rect(Window, Color, (X + 1, Y - W + 1, 19, 39), 0)
    # Go to the left cell
    elif(Direction == 'left') :
        pygame.draw.rect(Window, Color, (X - W + 1, Y + 1, 39, 19), 0)
    # Go to the bottom cell
    elif(Direction == 'down') :
        pygame.draw.rect(Window, Color, (X + 1, Y + 1, 19, 39), 0)
    # Go to the right cell
    elif(Direction == 'right') :
        pygame.draw.rect(Window, Color, (X + 1, Y + 1, 39, 19), 0)
    pygame.display.update()

def draw_next_cell_line(Window, X, Y, W, Direction, Color) :
    # Go to the top cell
    if(Direction == 'up') :
        pygame.draw.rect(Window, Color, (X + 1, Y - W + 1, 19, 20), 0)
    # Go to the left cell
    elif(Direction == 'left') :
        pygame.draw.rect(Window, Color, (X - W + 1, Y + 1, 20, 19), 0)
    # Go to the bottom cell
    elif(Direction == 'down') :
        pygame.draw.rect(Window, Color, (X + 1, Y + 1, 19, 20), 0)
    # Go to the right cell
    elif(Direction == 'right') :
        pygame.draw.rect(Window, Color, (X + 1, Y + 1, 20, 19), 0)
    pygame.display.update()

def draw_cells(Window, Start_x, Start_y, End_x, End_y, Color) :
    pygame.draw.rect(Window, Color, (Start_x + 1, Start_y + 1, End_x - Start_x - 1, End_y - Start_y - 1), 0)
