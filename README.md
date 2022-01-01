# Maze Generator
Small tool that generates mazes from different sizes, starting at 5x5 grid to 30x30 grid, using different algorithms. Coded in Python 🐍.

Currently, the tool only supports 4 algorithms (hoping to implement more!) :
* [First Depth Search](https://en.wikipedia.org/wiki/Depth-first_search).
* [Kruskal's algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm).
* [Prim's algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm).
* [Recursive Division](https://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_division_method)

Big shout out to Jamis Buck, your articles in [The Buckblog](http://weblog.jamisbuck.org/) really helped me to achieve this. Thanks a lot!

## Installing the project
Before installing the project, make sure you have [Python 3.8.6](https://www.python.org/downloads/release/python-386/) or later installed on your computer. After this, it is required to download the repository and to install [pygame](https://www.pygame.org/news), this library is required in order to make the project work.

```
> git clone https://github.com/GustavoRuedaEnriquez/maze-generator.git
> cd maze-generator
> pip install pygame
```

## Usage
The usage is really simple, on the project's directory run the command following this template:
```
> python maze-generator.py <width> <height> <algorithm>
```
Where:
* width - A number representing the total width in cells. Valid values are [5, 30].
* height - A number representing the total height in cells. Valid values are [5, 30].
* algorithm - A string representing the desired algorithm to use. Valid values [dfs, prim, kruskal].

*i.e.1. Generate a 15x21 maze using depth first search algorithm*
```
> python maze-generator.py 15 21 dfs
```

*i.e.2. Generate a 30x30 maze using prim's algorithm*
```
> python maze-generator.py 30 30 prim
```

<div align='center'>
<img src="./gifs/usage.gif" alt="Demo"/>
</div>
