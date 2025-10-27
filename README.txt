A* Path Finding Project by David Shapiro

How to Run:
- Ensure tkinter package is installed
- run python3 planner.py
- Answer question about including payload (in terminal)
- tkinter window will open. Press "Run Path Finder" to start
- if you wish, you can view the path plan in the "path.txt" file which is generated

Color Code:
Red square is robot (prechosen)
Pink is obstructions (randomly placed each time)
White is obstacles (pre-chosed locations)
Blue is goal state (prechosen)

Assumptions:
1) Used the manhattan distance heuristic
2) Chose the A* search algorithm
3) Each move between fiducials counts as a cost of 1
4) A move through an obstacle or obstruction counts as 100 to enter, move through and exit
5) Set the size of the board to 600x400 pixels
6) Placed fiducials every 40 pixels
7) Assuming robots don't need to turn orientation when moving in a new direction
8) Assuming robots can drive through obstacles/obstructions if no better option