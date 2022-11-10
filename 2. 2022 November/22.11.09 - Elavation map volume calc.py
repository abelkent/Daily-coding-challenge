# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 15:02:46 2022


Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

You are given an array of non-negative integers that represents a 
two-dimensional elevation map where each element is unit-width wall and the 
integer is the height. Suppose it will rain and all spots between two walls 
get filled up.

Compute how many units of water remain trapped on the map in O(N) time and 
O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the 
middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 
2 in the second, and 3 in the fourth index (we cannot hold 5 since it would 
run off to the left), so we can trap 8 units of water.

@author: abelw
"""

import math

#Naive approach with no concern for space-time complexity
#Works provided there are no "pockets"
def water_map(height_map):
    
    maximum = max(height_map)
    inverted_map = [(maximum - local_value) for local_value in height_map]
    print(inverted_map)
    while 0 in inverted_map:
        inverted_map.remove(0)
    
    if len(inverted_map) == 1:
        return sum(inverted_map)
    
    minimum = min(inverted_map)
    inverted_map = [(local_value - minimum) for local_value in inverted_map]
    print(inverted_map)
    
    return(sum(inverted_map))

test = water_map([4,2,3,5,2,5])
    
