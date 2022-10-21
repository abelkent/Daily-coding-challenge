# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 18:39:52 2022

@author: abelw
"""

def nonadjacent_max_finder(array):
    
    #Len = 0, return 0
    if len(array) == 0:
        return 0
    
    #Len = 1, return only element
    elif len(array) == 1:
        return array[0]
    
    #Len = 2+
    else:
        max_sum = array[:] #Initialise max_sum array
    
        #Len = 2, max_sum[1] = max of first 2 elements
        max_sum[1] = max(max_sum[0],max_sum[1])
        
        #Len 3+, repeat for each remaining element in array
        for index in range(2,len(array)):
            max_sum[index] = max(max_sum[index-1], max_sum[index-2] + array[index]) #max_sum element at that index set to the max(previous, previous^2 and current)
    
    return max_sum.pop()
    
test = nonadjacent_max_finder([7,10,12,7,9,14])