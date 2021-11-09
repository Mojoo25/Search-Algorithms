'''
This is a user-interactive multimode (multi search algorithm and multi grid set up) 
search algorithm testing tool. I started off with the code from the description in
this video. https://www.youtube.com/watch?v=JtiK0DOeI4A
'''

import pygame
from queue import PriorityQueue
import random
from collections import deque as queue 

WIDTH = 1000
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Mojo's Search Algorithm and Visualization test tool")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE 
        self.neighbors = [] 
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col
    
    def is_closed(self):
        return self.color == RED

    def is_open(self):
        
        return self.color == GREEN 
    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = ORANGE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_goal(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): #DOWN
            self.neighbors.append(grid[self.row + 1][self.col])
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): #UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2) 

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path() 
        draw()


def A_star(draw, grid, start, goal):
    count = 0
    nodes_Visited = 0
    open_set = PriorityQueue() 
    open_set.put((0, count, start)) 
    came_from = {} 
    g_score = {spot: float("inf") for row in grid for spot in row} 
    g_score[start] = 0 
    f_score = {spot: float("inf") for row in grid for spot in row} 
    f_score[start] = h(start.get_pos(), goal.get_pos())  
    
    open_set_hash = {start} 
    
    while not open_set.empty(): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                
        current = open_set.get()[2] 
        open_set_hash.remove(current)
        
        if current == goal:
            reconstruct_path(came_from, goal, draw) 
            goal.make_goal() 
            start.make_start()
            draw()
            print(f'The A_star algorithm for this grid visited {nodes_Visited} nodes to find a path')
            return True 
        
        for neighbor in current.neighbors: 
            temp_g_score = g_score[current] + 1 
            
            
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score 
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), goal.get_pos()) 
                if neighbor not in open_set_hash: 
                    count += 1 
                    open_set.put((f_score[neighbor], count, neighbor)) 
                    open_set_hash.add(neighbor) 
                    neighbor.make_open() 
                    
        draw() 
        
        if current != start: 
            current.make_closed()
            nodes_Visited += 1
            
    return False

def bfs(draw, grid, start, goal):
    q = queue()
    nodes_Visited = 0
    q.append(start)
    visited = {spot: False for row in grid for spot in row} 
    
    came_from = {} 
      
    
    
    
    while (len(q)> 0): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                
        current = q.popleft()
        visited[current] = True
        
        
        if current == goal:
            reconstruct_path(came_from, goal, draw) 
            goal.make_goal() 
            start.make_start()
            print(f'The bfs algorithm for this grid visited {nodes_Visited} nodes to find a path')
            return True 
        
        for neighbor in current.neighbors: 
            
            if neighbor not in q and visited[neighbor] == False:
                
                q.append(neighbor)
                neighbor.make_open() 
                came_from[neighbor] = current
                
            
                    
        draw() 
        
        if current != start: 
            
           
            current.make_closed()
            nodes_Visited += 1
            
    return False

def dfs(draw, grid, start, goal):
    q = queue()
    nodes_Visited = 0
    q.append(start)
    visited = {spot: False for row in grid for spot in row} 
    
    came_from = {} 
      
    
    
    
    while (len(q)> 0): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                
        current = q.pop()
        visited[current] = True
        
        
        if current == goal:
            reconstruct_path(came_from, goal, draw) 
            goal.make_goal() 
            start.make_start()
            print(f'The dfs algorithm for this grid visited {nodes_Visited} nodes to find a path')
            return True 
        
        for neighbor in current.neighbors: 
            
            if neighbor not in q and visited[neighbor] == False:
                
                q.append(neighbor)
                neighbor.make_open() 
                came_from[neighbor] = current
                
            
                    
        draw() 
        
        if current != start: 
            
           
            current.make_closed()
            nodes_Visited += 1
            
    return False



def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
    for j in range(rows):
        pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def main(win, width):
    
    print('''\n\n Welome to Mojo's Search Algorithm and Visualization test tool
          
          \n Press 'c'to clear (which resets the mode for 2-5), press r to restart the tool
          \n(After pressing 'r', just go into your console to input a new mode, even if pygame is 'not responding')
          
          \nFirstly, select the mode you would like to operate on
          \n1 - If you will like an interactive 50 x 50grid where you can select the start and goal nodes with the click
          of your mouse and set obstacles as you click a node. First click is the start, second click is the goal
          click further as much as you want for the obstacles, then start the tool
          \n 2 - If you want a randomly generated grid with randomly placed obstacles, start and goal positions
          \n 3 - If you want a randomly generated grid but start at origin and exit at last row
          \n 4 - If you want a randomly generated grid but start at origin and exit at last column
          \n 5 - If you want a randomly generated grid but want to choose your start and goal location
          \n Secondly, select  an algorithm to run
          \nBefore that save create map setup then press 's' to save map/grid
          Press 'b' on the keyboard to run bfs
          Press 'd' on Keyboard to run dfs
          press 'a' to run A_star algorithm
          Remember to press c between algorithms. Press r to selet new mode''')
    Running = True
    while Running :
        keepRunning = False
        while keepRunning == False:
            
            try:
                mode = int(input('Choose your mode, please: ' ))
                if mode <1 or mode > 5:
                    print ('You have entered a wrong mode, please select an integer between 1-5')
                else:
                    keepRunning = True
            
            except: 
                print ('You have entered a non-integer, please select an integer between 1-5')
            
        if mode == 1:
            ROWS = 50
            grid = make_grid(ROWS, width) 
            start = None
            goal = None
            run = True
            while run:
                draw(win, grid, ROWS, width)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        Running = False
        
                    if pygame.mouse.get_pressed()[0]: # LEFT 
                        pos = pygame.mouse.get_pos()
                        row, col = get_clicked_pos(pos, ROWS, width)
                       
                        spot = grid[row][col]
                        if not start and spot != goal:
                            start = spot
                            start.make_start()
        
                        elif not goal and spot != start:
                            goal = spot
                            goal.make_goal()
        
                        elif spot != goal and spot != start:
                            spot.make_barrier()
        
                    elif pygame.mouse.get_pressed()[2]: # RIGHT
                        pos = pygame.mouse.get_pos()
                        
                        row, col = get_clicked_pos(pos, ROWS, width)
                        
                        spot = grid[row][col]
                        spot.reset()
                        if spot == start:
                            start = None
                        elif spot == goal:
                            goal = None
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s :
                                pygame.image.save(win, 'mode1_map_setup.jpeg')
                        if event.key == pygame.K_a and start and goal:
                            for row in grid:
                                for spot in row:
                                    spot.update_neighbors(grid)
        
                            A_star(lambda: draw(win, grid, ROWS, width), grid, start, goal)
                            draw(win, grid, ROWS, width)
                            pygame.image.save(win, 'mode1_A_star.jpeg')
                        if event.key == pygame.K_b and start and goal:
                            for row in grid:
                                for spot in row:
                                    spot.update_neighbors(grid)
        
                            bfs(lambda: draw(win, grid, ROWS, width), grid, start, goal)
                            draw(win, grid, ROWS, width)
                            pygame.image.save(win, 'mode1_bfs.jpeg')
                        if event.key == pygame.K_d and start and goal:
                            for row in grid:
                                for spot in row:
                                    spot.update_neighbors(grid)
        
                            dfs(lambda: draw(win, grid, ROWS, width), grid, start, goal)
                            draw(win, grid, ROWS, width)
                            pygame.image.save(win, 'mode1_dfs.jpeg')
                        if event.key == pygame.K_c:
                            start = None
                            goal = None
                            grid = make_grid(ROWS, width)
                        if event.key == pygame.K_r:
                            start = None
                            goal = None
                            grid = make_grid(ROWS, width)
                            run = False
        elif mode == 2:
            ROWS = random.randrange(10,120,5)
            print('This is a randomly generated grid board with ', ROWS, 'rows and columns')
            grid = make_grid(ROWS, width) 
            spot = grid[random.randrange(0,ROWS-1)][random.randrange(0,ROWS-1)]
            start = spot
            spot = grid[random.randrange(0,ROWS-1)][random.randrange(0,ROWS-1)]
    
            if spot != start:
                goal = spot
                
    
            
            mode2barrier = random.randrange(1,30)* (ROWS//10) #This is number of barriers to be created
            #I let it be dependent on the size of the actual grid
            mode2barriernum = 0 #counter for number of barriers created
            barrierlist = []
            while mode2barriernum <= mode2barrier:
                spot = grid[random.randrange(0,ROWS-1)][random.randrange(0,ROWS-1)]
                barrierlist.append(spot)
                mode2barriernum +=1
            moderunning = True
            
            while moderunning:
                start.make_start()
                goal.make_goal()
                
                for obstacle in barrierlist:
                    obstacle.make_barrier()
                run = True
                while run:
                    
                    draw(win, grid, ROWS, width)        
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                            Running = False
                            moderunning = False
            
                        
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_s :
                                pygame.image.save(win, 'mode2_map_setup.jpeg')
                            if event.key == pygame.K_a and start and goal:
                                for row in grid:
                                    for spot in row:
                                        spot.update_neighbors(grid)
            
                                A_star(lambda: draw(win, grid, ROWS, width), grid, start, goal)
                                draw(win, grid, ROWS, width)
                                pygame.image.save(win, 'mode2_A_star.jpeg')
                            if event.key == pygame.K_b and start and goal:
                                for row in grid:
                                    for spot in row:
                                        spot.update_neighbors(grid)
            
                                bfs(lambda: draw(win, grid, ROWS, width), grid, start, goal)
                                draw(win, grid, ROWS, width)
                                pygame.image.save(win, 'mode2_bfs.jpeg')
                            if event.key == pygame.K_d and start and goal:
                                for row in grid:
                                    for spot in row:
                                        spot.update_neighbors(grid)
            
                                dfs(lambda: draw(win, grid, ROWS, width), grid, start, goal)
                                draw(win, grid, ROWS, width)
                                pygame.image.save(win, 'mode2_dfs.jpeg')
                            if event.key == pygame.K_c:
                                for row in grid:
                                        for spot in row:
                                            spot.reset()
                                run = False
                                
                            if event.key == pygame.K_r:
                                start = None
                                goal = None
                                grid = make_grid(ROWS, width)
                                run = False
                                moderunning = False
                    
                    
                    
                            
                
        elif mode == 3:
            ROWS = random.randrange(10,120,5)
            print('This is a randomly generated grid board with ', ROWS, 'rows and columns')
            grid = make_grid(ROWS, width) 
    
            start = grid[0][0]
            start.make_start()
            goal = grid[ROWS-1][random.randrange(0,ROWS-1)]
            goal.make_goal()
            mode3barrier = random.randrange(1,30)* (ROWS//10) #This is number of barriers to be created
            #I let it be dependent on the size of the actual grid
            mode3barriernum = 0 #counter for number of barriers created
            barrierlist = []
            while mode3barriernum <= mode3barrier:
                spot = grid[random.randrange(0,ROWS-1)] [random.randrange(0,ROWS-1)]
                                 
                if spot != goal and spot != start:
                    barrierlist.append(spot)
                    mode3barriernum +=1
            moderunning = True
            
            while moderunning:
                start.make_start()
                goal.make_goal()
                for obstacle in barrierlist:
                    obstacle.make_barrier()
                
                
                run = True
                while run:
                    draw(win, grid, ROWS, width)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                            moderunning = False
                            Running = False
            
                        
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_s :
                                pygame.image.save(win, 'mode3_map_setup.jpeg')
                            if event.key == pygame.K_a and start and goal:
                                for row in grid:
                                    for spot in row:
                                        spot.update_neighbors(grid)
            
                                A_star(lambda: draw(win, grid, ROWS, width), grid, start, goal)
                                draw(win, grid, ROWS, width)
                                pygame.image.save(win, 'mode3_A_star.jpeg')
                            if event.key == pygame.K_b and start and goal:
                                for row in grid:
                                    for spot in row:
                                        spot.update_neighbors(grid)
            
                                bfs(lambda: draw(win, grid, ROWS, width), grid, start, goal)
                                draw(win, grid, ROWS, width)
                                pygame.image.save(win, 'mode3_bfs.jpeg')
                            if event.key == pygame.K_d and start and goal:
                                for row in grid:
                                    for spot in row:
                                        spot.update_neighbors(grid)
            
                                dfs(lambda: draw(win, grid, ROWS, width), grid, start, goal)
                                draw(win, grid, ROWS, width)
                                pygame.image.save(win, 'mode3_dfs.jpeg')
            
                            if event.key == pygame.K_c:
                                
                                for row in grid:
                                    for spot in row:
                                        spot.reset()
                                run = False
                            if event.key == pygame.K_r:
                                start = None
                                goal = None
                                grid = make_grid(ROWS, width)
                                run = False
                                moderunning = False
                    
                
                    
        elif mode == 4:
            ROWS = random.randrange(10,120,5)
            print('This is a randomly generated grid board with ', ROWS, 'rows and columns')
            grid = make_grid(ROWS, width) 
            
            start = grid[0][0]
            start.make_start()
            goal = grid[random.randrange(0,ROWS-1)][ROWS-1]
            goal.make_goal()
            
            mode4barrier = random.randrange(1,30)* (ROWS//10) #This is number of barriers to be created
            #I let it be dependent on the size of the actual grid
            mode4barriernum = 0 #counter for number of barriers created
            
            barrierlist = []
            while mode4barriernum <= mode4barrier:
                spot = grid[random.randrange(0,ROWS)][random.randrange(0,ROWS)]
                
                if spot != goal and spot != start:
                    barrierlist.append(spot)
                    mode4barriernum +=1
            moderunning = True
            
            while moderunning:
                start.make_start()
                goal.make_goal()
                for obstacle in barrierlist:
                    obstacle.make_barrier()
                run = True
                while run:
                    draw(win, grid, ROWS, width)
                    
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                            Running = False
                            moderunning = False
            
                        
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_s :
                                pygame.image.save(win, 'mode4_map_setup.jpeg')
                            if event.key == pygame.K_a and start and goal:
                                for row in grid:
                                    for spot in row:
                                        spot.update_neighbors(grid)
            
                                A_star(lambda: draw(win, grid, ROWS, width), grid, start, goal)
                                draw(win, grid, ROWS, width)
                                
                                pygame.image.save(win, 'mode4_A_star.jpeg')
                            if event.key == pygame.K_b and start and goal:
                                for row in grid:
                                    for spot in row:
                                        spot.update_neighbors(grid)
            
                                bfs(lambda: draw(win, grid, ROWS, width), grid, start, goal)
                                draw(win, grid, ROWS, width)
                                pygame.image.save(win, 'mode4_bfs.jpeg')
                            if event.key == pygame.K_d and start and goal:
                                for row in grid:
                                    for spot in row:
                                        spot.update_neighbors(grid)
            
                                dfs(lambda: draw(win, grid, ROWS, width), grid, start, goal)
                                draw(win, grid, ROWS, width)
                                pygame.image.save(win, 'mode4_dfs.jpeg')
                            if event.key == pygame.K_c:
                                for row in grid:
                                    for spot in row:
                                        spot.reset()
                                run = False
                            if event.key == pygame.K_r:
                                start = None
                                goal = None
                                grid = make_grid(ROWS, width)
                                run = False
                                moderunning = False
        elif mode == 5:
            ROWS = random.randrange(10,120,5)
            print('This is a randomly generated grid board with ', ROWS, 'rows and columns')
            grid = make_grid(ROWS, width) 
            start = None
            goal = None
            
            
            
            
            # start_row = int(input(f'please enter your desired start row between 0 and {ROWS}: '))
            # start_col = int(input(f'please enter your desired start column between 0 and {ROWS}: '))  
            # stop_row = int(input(f'please enter your desired goal row between 0 and {ROWS}: '))
            # stop_col = int(input(f'please enter your desired goal column between 0 and {ROWS}: '))
            # start = grid[start_row][start_col]
            # start.make_start()
            # goal = grid[stop_row][stop_col]
            # goal.make_goal()
            
            mode5barrier = random.randrange(1,30)* (ROWS//10) #This is number of barriers to be created
            #I let it be dependent on the size of the actual grid
            mode5barriernum = 0 #counter for number of barriers created
            barrierlist = []
            while mode5barriernum <= mode5barrier:
                spot = grid[random.randrange(0,ROWS)][random.randrange(0,ROWS)]
                
                # if spot != goal and spot != start:
                barrierlist.append(spot)
                mode5barriernum +=1
            
                    
            moderunning = True
            
            while moderunning:
                
                for obstacle in barrierlist:
                    obstacle.make_barrier()
                run = True
                while run:
                    draw(win, grid, ROWS, width)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                            Running = False
                            moderunning = False
            
                        if pygame.mouse.get_pressed()[0]: # LEFT 
                            pos = pygame.mouse.get_pos()
                            row, col = get_clicked_pos(pos, ROWS, width)
                            
                            spot = grid[row][col]
                            if not start and spot != goal:
                                start = spot
                                start.make_start()
            
                            elif not goal and spot != start:
                                goal = spot
                                goal.make_goal()
    
            
                        elif pygame.mouse.get_pressed()[2]: # RIGHT
                            pos = pygame.mouse.get_pos()
                           
                            row, col = get_clicked_pos(pos, ROWS, width)
                            
                            spot = grid[row][col]
                            spot.reset()
                            if spot == start:
                                start = None
                            elif spot == goal:
                                goal = None
                                        
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_s :
                                pygame.image.save(win, 'mode5_map_setup.jpeg')
                            if event.key == pygame.K_a and start and goal:
                                for row in grid:
                                    for spot in row:
                                        spot.update_neighbors(grid)
            
                                A_star(lambda: draw(win, grid, ROWS, width), grid, start, goal)
                                draw(win, grid, ROWS, width)
                                pygame.image.save(win, 'mode5_A_star.jpeg')
                            if event.key == pygame.K_b and start and goal:
                                for row in grid:
                                    for spot in row:
                                        spot.update_neighbors(grid)
            
                                bfs(lambda: draw(win, grid, ROWS, width), grid, start, goal)
                                draw(win, grid, ROWS, width)
                                pygame.image.save(win, 'mode5_bfs.jpeg')
                            if event.key == pygame.K_d and start and goal:
                                for row in grid:
                                    for spot in row:
                                        spot.update_neighbors(grid)
            
                                dfs(lambda: draw(win, grid, ROWS, width), grid, start, goal)
                                draw(win, grid, ROWS, width)
                                pygame.image.save(win, 'mode5_dfs.jpeg')
                            if event.key == pygame.K_c:
                                for row in grid:
                                    for spot in row:
                                        spot.reset()
                                run = False
                            if event.key == pygame.K_r:
                                start = None
                                goal = None
                                grid = make_grid(ROWS, width)
                                run = False
                                moderunning = False
                    
                    
        

    pygame.quit()




    
main(WIN, WIDTH)
