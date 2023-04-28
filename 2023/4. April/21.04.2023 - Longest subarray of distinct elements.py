"""
Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].
"""

example_array = [5, 1, 3, 5, 2, 3, 4, 1]

def subarray_finder(array):

    maximum_array = list()

    local_subarray = list()
    for element in array:
        local_subarray.append(element)
        
        local_subset = set(local_subarray)
        if len(local_subarray) != len(local_subset):
            if len(maximum_array) < len(local_subarray):
                maximum_array = local_subarray
            
            while True:
                local_subarray.pop(0)
                local_subset = set(local_subarray)
                
                if len(local_subarray) == len(local_subset):
                    break
    
    return maximum_array

print(subarray_finder(example_array))