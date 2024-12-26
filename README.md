# Maze Generator
Tool that generates mazes from different sizes, starting at 5x5 grid to 40x40 grid, using different algorithms. Coded in Python 🐍.

Additionally, this tool also allows to save mazes as text files (.maze files), this functionality is useful when trying to recreate a past maze, because the tool also allows to input a .maze file and draw the maze this file represents.

Currently, these 4 algorithms are supported:
* [First Depth Search](https://en.wikipedia.org/wiki/Depth-first_search).
* [Kruskal's algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm).
* [Prim's algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm).
* [Recursive Division](https://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_division_method)
* [Eller's algorithm](http://www.neocomputer.org/projects/eller.html)

Special mention to Jamis Buck, your articles in [The Buckblog](http://weblog.jamisbuck.org/) really helped me to achieve this. Thanks a lot!

## Running the project
Make sure you have [Python 3.8.6](https://www.python.org/downloads/release/python-386/) or later installed on your computer. After this, download the repository and install [pygame](https://www.pygame.org/news), this library is required in order for the project to work.

```
> git clone https://github.com/GustavoRuedaEnriquez/maze-generator.git
> cd maze-generator
> pip install pygame
```

## Usage
### Creating a custom maze
On project's main directory run the following:
```
> python maze-generator.py --size <width>x<height> --algorithm <algorithm>
```
Where:
* width - Number representing total width in cells.
* height - Number representing total height in cells.
* algorithm - String representing the desired algorithm to use.

*example. Generate a 15x21 maze using depth first search algorithm*
```
> python maze-generator.py --size 15x21 --algorithm dfs
```

<div align='center'>
<img src="./gifs/usage.gif" alt="Demo"/>
</div>

If you want to save your maze as a text file, you can do it using the `--write`
argument.

*example Generate a 30x30 maze using prim's algorithm and write the generated maze on `custom_maze.maze`*
```
> python maze-generator.py --size 30x30 --algorithm prim --write custom_maze
```
Arguments have a short short version too, use to `--help` or `-h` argument to see all the details.