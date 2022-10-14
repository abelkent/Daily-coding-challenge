# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 15:11:30 2022

@author: abelw
"""

def list_sum(array, total):
    for a in range(len(array)):
        element_a = array.pop(0)
        for index in range(len(array)):
            element_b = array[index]
            if (element_a + element_b) == total:
                return True
    
    return False
            
        
test = list_sum([10, 15, 3, 7], 17)
        