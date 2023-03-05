"""
Given an array of numbers and an index i, return the index of the nearest larger number of the number at index i, 
where distance is measured in array indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

If two distances to larger numbers are the equal, then return any one of them. 
If the array at i doesn't have a nearest larger integer, then return null.
"""

def nearest_large_finder(array, starting_index):
    
    value_to_beat = array[starting_index]

    #Left check
    def left_check(starting_index):
        distance = int(1)
        for index in range(starting_index-1,-1,-1):
            if array[index] > value_to_beat:
                return (distance)
            else:
                distance += 1
    
        return (None)
    
    def right_check(starting_index):
        distance = int(1)
        for index in range(starting_index+1, len(array),1):
            if array[index] > value_to_beat:
                return (distance)
            else:
                distance += 1
        
        return (None)

    left, right = left_check(starting_index), right_check(starting_index)

    if (left == None) and (right == None):
        return None
    
    if left == None:
        return right
    elif right == None:
        return left
    else:
        return min(left, right)

print(nearest_large_finder([4, 1, 3, 5, 6], 0))
