"""
Given an array of integers out of order, determine the bounds of the 
smallest window that must be sorted in order for the entire array to be sorted.

For example, given [3, 7, 5, 6, 9], you should return (1, 3).
"""

import math

#Inspired by solution found at: https://www.techiedelight.com/smallest-window-sorting-which-make-array-sorted/
def window_finder(array):
    current_maximum = int(0)
    current_minimum = math.inf

    maximum_break_index = int()
    minimum_break_index = int()

    #Traverse left to right until an element that is lower than maximum (up to that point)
    #NOTE: You keep track of the changes of the last detected alteration until the end of the propogation
    #NOTE cont: We need to know the last point at which the pattern breaks
    for index in range(len(array)):
        if array[index] > current_maximum:
            current_maximum = array[index]
        
        if array[index] < current_maximum:
            maximum_break_index = int(index)
    
    for index in range(len(array)-1,-1,-1):
        if array[index] < current_minimum:
            current_minimum = array[index]
        
        if array[index] > current_minimum:
            minimum_break_index = int(index)
    
    return(minimum_break_index, maximum_break_index)

print(window_finder([3, 7, 5, 6, 9]))
