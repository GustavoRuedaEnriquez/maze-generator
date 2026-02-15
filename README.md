# Maze Generator
Maze Generator is a Command Line Interface (CLI) utility for generating and solving mazes using multiple algorithms — complete with animated visualization.
Coded in Python 🐍.

## Features 🚀
### Maze Generation
Generate mazes using 5 different generation algorithms:
- [First Depth Search](https://en.wikipedia.org/wiki/Depth-first_search).
- [Kruskal's algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm).
- [Prim's algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm).
- [Recursive Division](https://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_division_method)
- [Eller's algorithm](http://www.neocomputer.org/projects/eller.html)

Each algorithm:
- Creates a fully connected maze.
- Produces unique layouts.
- Displays a real-time generation animation of how the maze is being generated.

Special mention to Jamis Buck, his articles in [The Buckblog](http://weblog.jamisbuck.org/) really helped to achieve this. Thanks a lot!

### Maze Solving
Visualize how a maze can be solved using different pathfinding strategies:
- [A* A-Star search](https://en.wikipedia.org/wiki/A*_search_algorithm)

Each solver:
- Animates the search process
- Shows visited cells
- Highlights the final path from start to goal

### Maze Object Representation
Every generated maze is stored as an object with 3 attributes:
```
  "width": <int>,
  "height": <int>,
  "matrix": [[0, 1, 1, 0, ...], ...]
```
Where:
* `width` - Maze width
* `height` - Maze height
* `matrix` -  2D grid representation
  * `0` = Wall
  * `1` = Path

This object can be saved into a text file to be used later.

## Installation 🖥️
Make sure you have [Python 3.8.6](https://www.python.org/downloads/release/python-386/) or later installed on your computer. After this, download the repository and install [pygame](https://www.pygame.org/news), this library is required in order for the project to work.

```
> git clone https://github.com/GustavoRuedaEnriquez/maze-generator.git
> cd maze-generator
> pip install pygame
```

## Usage
### Generate maze
On project's main directory run the following:
```
python maze-generator.py --maze-size [WIDTH]x[HEIGHT] --generation-algorithm [GEN-ALGORITHM]
```
Where:
* `[WIDTH]` - Total width in cells.
* `[HEIGHT]` - Total height in cells.
* `[GEN-ALGORITHM]` - Desired maze generation algorithm to use.

*Example - Generate a 15x21 maze using depth first search algorithm*
```
python maze-generator.py --maze-size 15x21 --generation-algorithm dfs
```
### Generate maze and solve it
On project's main directory run the following:
```
python maze-generator.py --maze-size [WIDTH]x[HEIGHT] --generation-algorithm [GEN-ALGORITHM] --solving-algorithm [SOL-ALGORITHM]
```
Where:
* `[WIDTH]` - Total width in cells.
* `[HEIGHT]` - Total height in cells.
* `[GEN-ALGORITHM]` - Desired maze generation algorithm to use.
* `[SOL-ALGORITHM]` - Desired pathfinding algorithm to use.

*Example - Generate a 40x37 maze using Prim's algorithm and solve it using A-Star algorithm*
```
python maze-generator.py --maze-size 40x37 --generation-algorithm prim --solving-algorithm a_star
```

### Generate maze and save it into a text file
On project's main directory run the following:
```
python maze-generator.py --maze-size [WIDTH]x[HEIGHT] --generation-algorithm [GEN-ALGORITHM] --maze-write [WRITE_PATH]
```
Where:
* `[WIDTH]` - Total width in cells.
* `[HEIGHT]` - Total height in cells.
* `[GEN-ALGORITHM]` - Desired maze generation algorithm to use.
* `[WRITE-PATH]` - Desired path where the output text file will be saved.

*Example - Generate a 23x15 maze using Kruskal's algorithm and save it on "./my_maze" text file*
```
python maze-generator.py --maze-size 23x15 --generation-algorithm kruskal --maze-write ./my_maze
```
**IMPORTANT:** The output file will be saved with the file extension `.maze`

### Load maze text file and display it
On project's main directory run the following:
```
python maze-generator.py --maze-source [SOURCE_PATH]
```
Where:
* `[SOURCE-PATH]` - Desired path where the output text file will be saved.

*Example - Display maze saved on custom_maze.maze*
```
python maze-generator.py --maze-source custom_maze.maze
```

### Load maze text file, display it and solve it
On project's main directory run the following:
```
python maze-generator.py --maze-source [SOURCE_PATH] --solving-algorithm [SOL-ALGORITHM]
```
Where:
* `[SOURCE-PATH]` - Desired path where the output text file will be saved.
* `[SOL-ALGORITHM]` - Desired pathfinding algorithm to use.

*Example - Display maze saved on custom_maze.maze and solve it using A-Star algorithm*
```
python maze-generator.py --maze-source custom_maze.maze --solving-algorithm a_star
```
Arguments have a short short version too, use `--help` or `-h` argument to see all the details.