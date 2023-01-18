"""
You are in an infinite 2D grid where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points. 
Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:

Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2)
"""

#Defines function
def minimum_steps(sequence):

    #Initialises current position to first element in sequence
    x_current = sequence[0][0]
    y_current = sequence[0][1]

    #Initialises step count at 0
    step_count = int(0)

    #Iterates through each following element in sequence as new destination
    for destination in sequence[1:]:
        print("New destination: "+str(destination))
        #Destination is set as goal co-ordinates
        x_goal, y_goal = destination[0], destination[1]
        
        #While current position is not equal to goal position...
        while (x_current != x_goal) or (y_current != y_goal):

            print("Current position: "+str(x_current) + " " + str(y_current))
            #x and y change are set to zero
            x_change, y_change = int(0),int(0)

            #Updates x and y change based on relative position of destination
            if (x_current < x_goal):
                x_change = 1
            elif (x_current > x_goal):
                x_change = -1
            
            if (y_current < y_goal):
                y_change = 1
            elif (y_current > y_goal):
                y_change = -1
            
            #If x or y have been changed, updates step count
            if (x_change != 0) or (y_change != 0):
                step_count += 1
            
            #Updates position
            x_current += x_change
            y_current += y_change

            print("END OF TURN, CURRENT POSITION: "+str(x_current) + " " + str(y_current))

    #Returns steps taken to user
    print("Total steps = " +str(step_count))

minimum_steps([(0, 0), (1, 1), (1, 2), (1,3)])
