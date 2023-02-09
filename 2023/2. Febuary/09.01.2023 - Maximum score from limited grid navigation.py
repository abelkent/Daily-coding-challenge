"""
You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start at matrix[0][0], and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1
The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.


"""

matrix = [
    [0, 3, 1, 1],
    [2, 0, 0, 4],
    [1, 5, 3, 1]
]

def matrix_navigator(matrix):

    #Definition of recursive step function
    def step(x_coord, y_coord, total = 0):

        #total incremented by value at each tile in grid
        total += matrix[y_coord][x_coord]

        #If step has reached the end of the matrix, return total
        if (x_coord == len(matrix[0])-1) and (y_coord == len(matrix)-1):
            return total

        #Otherwise...
        else:
            
            #If x has reached right wall, horizontal is set to 0, otherwise set as the step in that direction
            if (x_coord == len(matrix[0])-1):
                horizontal = int(0)
            else:
                horizontal = step(x_coord+1, y_coord, total)
            
            #If y has reached bottom, vertical is set to 0, otherwise set as the step in that direction
            if (y_coord == len(matrix)-1):
                vertical = int(0)
            else:
                vertical = step(x_coord, y_coord+1, total)
            
            #Returns maximum value of horizontal or verical step
            return max(horizontal, vertical)
    
    #Prints output to user from 0,0 starting position
    print(step(0,0))
        
matrix_navigator(matrix)
