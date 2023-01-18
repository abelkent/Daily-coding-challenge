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

def minimum_steps(sequence):

    x_current = sequence[0][0]
    y_current = sequence[0][1]

    step_count = int(0)

    for destination in sequence[1:]:
        print(destination)
        x_goal, y_goal = destination[0], destination[1]
        
        while (x_current != x_goal) and (y_current != y_goal):
            print(x_current,y_current)
            step_this_turn = bool(False)
            x_new = x_current
            y_new = y_current

            if x_goal > x_current:
                x_new += 1
                step_this_turn = True
            
            elif x_goal < x_current:
                x_new -= 1
                step_this_turn = True
            
            if y_goal > y_current:
                y_new += 1
                step_this_turn = True
            
            elif y_goal < y_current:
                step_this_turn = True
            
            if step_this_turn == True:
                step_count += 1
                x_current, y_current = x_new,y_new

    print("Total steps = " +str(step_count))

minimum_steps([(0, 0), (1, 1), (1, 2), (1,3)])
