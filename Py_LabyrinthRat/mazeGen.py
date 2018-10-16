'''
Created on 2018.06.04
@author: Ivana_ShineMo
'''

def valid(maze, x,y):
    # identify the point is walkable
    if (x>=0 and x<= len(maze) and y >= 0 and y <= len(maze(0)) and maze[x][y] == 1):
        return True
    else:
        return False
    
def walk(maze,x,y):
    # get the exit of the maze
    if (x== len(maze) and maze(x,y) == 1):
        print("Success!")
        return True
    
    if valid(maze, x, y):
        print(x,y)
        maze[x][y] = 2
        if not walk(maze, x-1, y):
            maze[x][y] = 1
        if not walk(maze, x+1, y):
            maze[x][y] = 1
        if not walk(maze, x, y-1):
            maze[x][y] = 1
        if not walk(maze, x, y+1):
            maze[x][y] = 1
        else:
            return False
    
    return True
    
maze=[[1,0,0,1,0,1],
      [1,1,1,0,1,0],
      [0,0,1,0,1,0],
      [0,1,1,1,0,0],
      [0,0,0,1,0,0],
      [1,0,0,0,0,0]]

walk(maze, 3, 3)                