"""
Given an integer list where each number represents the number of hops you can make, 
determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
"""

def array_hopper(array):

    position = int(0)

    while position != len(array)-1:

        if array[position] == 0:
            return False
        
        else:
            position += array[position]
    
    return True

print(array_hopper([2, 0, 1, 0]))
print(array_hopper([1, 1, 0, 1]))