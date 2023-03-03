"""
Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice,
find the two elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.
"""

#Had a couple of different ideas, will try some of them out and test speed

import time

def duplicator_locator(array):
    stack = list()
    for element in array:
        if element not in stack:
            stack.append(element)
        else:
            stack.remove(element)
        
    
    return stack

print(duplicator_locator([2, 4, 6, 8, 10, 2, 6, 10]))
