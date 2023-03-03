"""
Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice,
find the two elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.
"""

#Had a couple of different ideas, will try some of them out and test speed

import time

def duplicator_locator_stack(array):
    stack = list()
    for element in array:
        if element not in stack:
            stack.append(element)
        else:
            stack.remove(element)
    
    return stack

before = time.time()
print(duplicator_locator_stack([2, 4, 6, 8, 10, 2, 6, 10]))
after = time.time()
print(after - before)

"""def duplicator_locator_sorted(array):
    cache = list([None,None])
    array = sorted(array)
    print(array)


duplicator_locator_sorted([2, 4, 6, 8, 10, 2, 6, 10])
"""


