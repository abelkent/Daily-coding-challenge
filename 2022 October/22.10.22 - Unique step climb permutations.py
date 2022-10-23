# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 17:22:26 2022

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. 
Given N, write a function that returns the number of unique ways you can climb the staircase. 
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

@author: abelw
"""

def unique_climbs_test(N, index = 0):
    array = [1]*N
    
    def recursion(array):
        
        if len(array) == 0:
            return 0
    
        elif len(array) == 1:
            return 1
        
        elif len(array) == 2:
            return 2

        else:
            return recursion(array[1:]) + recursion(array[2:])
    
    return recursion(array)

def unique_climbs(N, set_of_steps):
    
    array = [1]*N
    smallest = min(set_of_steps)
    largest = max(set_of_steps)
    possible_variants = len(set_of_steps)
    set_of_steps.sort()
    print(set_of_steps)
    
    new_array = []
    for element in array:
        new_array.append():
            
    

                    
    
    return recursion(array)

test = unique_climbs(4, [1,2])