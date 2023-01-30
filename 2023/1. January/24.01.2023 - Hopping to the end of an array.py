"""
Given an integer list where each number represents the number of hops you can make, 
determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
"""

def array_hopper(array):

    #Initialises position at zero
    position = int(0)

    #While position is not equal to length of input minus 1 (ie, the final position in array), iterates through the following:
    while position != len(array)-1:

        #If value of array at position is zero (ie, no more jumps can be made), return False
        if array[position] == 0:
            return False
        
        #Position updated otherwise
        else:
            position += array[position]
    
    #Return True if condition is met
    return True

print(array_hopper([2, 0, 1, 0]))
print(array_hopper([1, 1, 0, 1]))