'''
You are running a gravity simulation involving falling boxes and
exploding obstacles. The scenario is represented by a
rectangular matrix board of characters:
'-' → Empty cell
'*' → Obstacle
'#' → Box


Rules:
1.Boxes fall down simultaneously as far as possible, until they hit:
    An obstacle (*)
    Another grounded box (#)
    The bottom of the board
2.If a box hits an obstacle (*), it explodes:
    The box destroys itself.
    Any boxes within 8 surrounding cells are also destroyed.
    All explosions happen simultaneously.

Task:
Write a function to return the state of the board after all boxes have fallen and explosions have occurred.

Example 1:
Input:
board = [['#', '-', '#', '#', '*'],
         ['#', '-', '-', '#', '#'],
         ['-', '#', '-', '#', '-'],
         ['-', '-', '#', '-', '#'],
         ['#', '*', '-', '-', '-'],
         ['-', '-', '*', '#', '-']]
Output:
        [['-', '-', '-', '-', '*'],
         ['-', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-'],
         ['-', '*', '-', '-', '#'],
         ['#', '-', '*', '-', '#']]
Example 2:
Input:
board = [['#', '#', '*'],
         ['#', '-', '*'],
         ['#', '-', '*'],
         ['-', '#', '#'],
         ['*', '-', '#'],
         ['*', '-', '-'],
         ['*', '-', '-']]
Output:
        [['-', '-', '*'],
         ['-', '-', '*'],
         ['-', '-', '*'],
         ['-', '-', '-'],
         ['*', '-', '-'],
         ['*', '-', '#'],
         ['*', '-', '#']]
'''
from collections import deque
from typing import List

'''
Workflow Timestamps
1. Make Sure You Understand the Problem
Ex1: board = [["*","#","-"]]
o/p: [["*","#","-"]]

Ex2: board =[["#","-","-]]
o/p: [["-","-","#"]]

Ex3: board = [["#","-","#"],
             ["-","#","-"],
             ["-","*","*"]]
    o/p:     [["-","-","-"],
             ["-","-","-"],
             ["-","*","*"]]
2. Design and Verify a Solution
            0  1   2
board = 0["#","-","#"],
        1["-","-","-"],
        2["-","#","*"]
        3["#","*","-"],
        4["*","-","-"]
        
        
        
        
        
        if cur_col is last column, remove from queue
        next_row,next_col = (0,1)
        if the next_row and next_col is empty and not in neighbours list, swap values, if in neighbours list make it empty
        if the next_row and next_col is obstacle, make cur_row,cur_col as empty in the grid and
            find out the 8 neighbours and add them to neighbours list
        
        0["#","-","-"],
        1["#","-","-"],
        2["-","#","*"]
        3["","*","-"],
        4["#","-","-"]
        
        queue = [(3,0)]
        cur_row,cur_col = (3,0)
        neighbours = []
        
         
        
             
- If we have only one row, return as it is
- Traverse through the grid and add the box position to the queue
-Perform the operation on queue until queue is empty
    -Define the neighbours to be exploded list as empty
    -Traverse through the queue
        -Check the cur row is last row, and in neighbour list, make it empty cell and remove them from the queue
        -Check if the next row where the box will fall has empty space in the grid and not in the neighbours list, 
            swap values, if in neighbours list make it empty and add the updated values back to the queue if its not in neighbours list
        -check if the next_row and next_col is box, then add cur row and cur col back to the queue
        -orelse if the next_row and next_col is obstacle, make cur_row,cur_col as empty in the grid and
            find out the 8 neighbours and add them to neighbours list and add the remove from the queue
            
    
    Time Complexity:O(m*n)
    Space Complexity:O(m*n)
    
3. Write the Code And Pass Test Cases.
'''

class Solution:

    def gravity_simulation(self,grid:List[List]):
        rows = len(grid)
        cols = len(grid[0])


        if rows == 1:
            return grid

        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "#":
                    queue.append((row, col))


        #          [['#', '-', '#', '#', '*'],
        #          ['#', '-', '-', '#', '#'],
        #          ['#', '#', '-', '#', '-'],
        #          ['#', '-', '#', '-', '#'],
        #          ['#', '*', '-', '-', '-'],
        #          ['#', '-', '*', '#', '-']]
        while queue:

            colliding_neighbours = set()
            boxes_range = len(queue)
            k = 0


            while k < boxes_range and queue:


                cur_row, cur_col = queue.popleft()
                next_row,next_col = cur_row +1, cur_col

                if cur_row == rows-1:
                    if (cur_row,cur_col) in colliding_neighbours:
                        grid[cur_row][cur_col] = "-"

                elif grid[next_row][next_col] == "-":
                    if (next_row,next_col) not in colliding_neighbours:
                        grid[next_row][next_col] = "#"
                        queue.append((next_row,next_col))

                    grid[cur_row][cur_col] = "-"
                elif grid[next_row][next_col] == "#":
                    if (next_row, next_col) in list(queue):
                        queue.append((cur_row, cur_col))
                        k -= 1
                    else:
                        break
                else:
                    grid[cur_row][cur_col] = "-"
                    for i,j in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]:
                        new_row = next_row + i
                        new_col = next_col + j

                        if new_row >=0 and new_col >= 0 and new_row < rows and new_col < cols and grid[new_row][new_col] == "#":

                            colliding_neighbours.add((new_row, new_col))
                            grid[new_row][new_col] = "-"
                k += 1

        return grid






s = Solution()
output = s.gravity_simulation([['#', '-', '#', '#', '*'],
         ['#', '-', '-', '#', '#'],
         ['-', '#', '-', '#', '-'],
         ['-', '-', '#', '-', '#'],
         ['#', '*', '-', '-', '-'],
         ['-', '-', '*', '#', '-']])

# output = s.gravity_simulation([["#","-","#"],
#              ["-","#","-"],
#              ["-","*","*"]])
print(output)












