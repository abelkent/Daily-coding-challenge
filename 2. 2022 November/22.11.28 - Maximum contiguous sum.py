"""
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
"""

def contiguous_sum(array):
    #Initialises max_so_far & max_ending_here as 0
    max_so_far = int(0)
    max_ending_here = int(0)

    #Iterates through all elements in input array
    for element in array:
        #max_ending_here incremented by element value
        max_ending_here += element

        #If max_ending_here is less than 0, is reset to 0 (as this means the accumulated value is now higher if set to the sum of nothing)
        if max_ending_here < 0:
            max_ending_here = 0
        
        #If max_so_far is less than max_ending_here, value is set to equal max_ending_here
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
    
    #After looping, sets max_so_fars value to max_ending_here, if that value is higher
    if (max_so_far < max_ending_here):
        max_so_far = max_ending_here
    
    #Returns max_so_far
    return max_so_far

print(contiguous_sum([34, -50, 42, 14, -5, 86]))
print(contiguous_sum([-5, -1, -8, -9]))