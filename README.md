# Search-Algorithms

This is basically a Search Algorithm testing tool I made starting with the code of this person: https://www.youtube.com/watch?v=JtiK0DOeI4A

This code was for an assignment in 'Intro to Mobile Robotics'. Therefore, I didn't focus too much on presentation of the code and other general consumer-friendliness of the 
user-interaction. However, the program has instructions

It took me about 24 hours of consistent work over two days to do this. When I started coding the program, I was proficient enough in Python but knew nothing about Pygame


Minimum Required FUnctionalities: 

1. Provide user with the following choices for search space
  a. Empty grid space where user can place obstacles, start location, and goal location
  b. Randomly generated maze (maze and/or grid with randomly placed obstacles).
    i. Randomize start, goal locations.
    ii. Start at origin, exit at last row, last column
    iii. Allow user choice of start, goal location
2. Loading and saving search spaces

   a. Allow user to save maze/grid to a file before running search algorithms. After a grid map is generated, it is convenient to save the grid and reuse it later when comparing   the performance of various algorithms.
  b. Allow user to load maze/grid from a file before running search algorithms.
  c. After running the search algorithm, allow user to save the result as an image file. This is convenient for later performance analysis.
3. Implement the following search algorithms
  a. Depth-first search
  b. Breadth-first search
  c. A*
    i. Assume diagonal movement is not allowed.
  d. Graduate students: implement greedy breadth-first search (https://en.wikipedia.org/wiki/Best-first_search)
4. Visualization
  a. As an algorithm is running, provide the user with feedback, text-based console output and through use of color when drawing cells.
  b. When algorithm finishes,
  i. Has a path been found?
  ii. If found,
    1. What is the path?
    2. What is the cost of the path?
    3. How may cells were visited while the algorithm ran?
    
    
Next, I will go through the minimum required functionalities and describe how or if I could cater for them:
1.	I created 5 user-selectable modes in the program to cater for the 5 different modes of assignment of grid size, start, goal and obstacle nodes. The code has more description   to the modes. The user can input ‘r’ from the keyboard anytime (except when an algorithm is running) to try to select another mode
2.	I couldn’t figure out how to save and load search spaces. Instead of saving and loading search spaces, I made each mode semi-resettable. Whichever way the mode assigns          start, goal and obstacle nodes, the locations of these modes are stored. After an algorithm is run, to go back to the original maze/search space, all grid cells are made        white and the stored start, end and obstacle nodes are re drawn (with the color) by pressing ‘c’
3.	The search algorithms are implemented. Due to time constraints, I couldn’t learn greedy BFS to implement.
4.	While no actual text based real time feedback (as I couldn’t figure out what exactly we might want to report back to the user) was implemented, visual feedback was         
	  implemented. Red cells are visited cells and green cells were open for visiting. If a path is found, it is drawn in purple. The number of cells visited are printed though 
    and the cost of traversal (each cell costs 1 to visit up/down or left/right
**Current challenges:**

•	I think my dfs is not working exactly as it should but no time to fix it now. I think it is actually supposed to traverse twice the number of node it traverses. 
•	Also, my mode one completely resets if I press c, so I have to manually reconstruct it for each algorithm. This would be hard to do, hence I won’t restart but just run each mode and take the screenshots in python. The screenshots may have visited nodes still marked from the previously ran algorithm but the amount of nodes visited would be an accurate way to compare the performance of each algorithm. I would run the algorithms in ascending order of grid pervasiveness, this should for the most part combat the issue of visited nodes from previous algorithm remaining in the screenshot. Other modes work perfectly though.

