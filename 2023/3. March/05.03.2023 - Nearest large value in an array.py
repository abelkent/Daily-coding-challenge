"""
Given an array of numbers and an index i, return the index of the nearest larger number of the number at index i, 
where distance is measured in array indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

If two distances to larger numbers are the equal, then return any one of them. 
If the array at i doesn't have a nearest larger integer, then return null.
"""

def nearest_large_finder(array, starting_index):
    
    #Retrieves value to beat from array and provided index
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
    
    #Right check
    def right_check(starting_index):
        distance = int(1)
        for index in range(starting_index+1, len(array),1):
            if array[index] > value_to_beat:
                return (distance)
            else:
                distance += 1
        return (None)

    #Sets left and right as the minimal distance to a larger value on the left and right of the given index provided respectively
    left, right = left_check(starting_index), right_check(starting_index)

    #If both are None, ie, there is no larger value - returns None
    if (left == None) and (right == None):
        return None
    
    #If only one of them is None, return the other
    if left == None:
        return right
    elif right == None:
        return left
    
    #Otherwise returns minimum value of the two
    else:
        return min(left, right)

print(nearest_large_finder([4, 1, 3, 5, 6], 0))
