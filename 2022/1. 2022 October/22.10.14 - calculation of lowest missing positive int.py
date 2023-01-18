# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 16:43:39 2022

@author: abelw
"""

def missing_int(array):
    array.sort()
    for item in array:
        if item <= 0:
            array.remove(item)
    data = list(set(iter(array)))
    
    for index in range(len(data)):
        if data[index] != index+1:
            return (index+1)
    
test_data = [3, 4, -1, 1]

test = missing_int(test_data)