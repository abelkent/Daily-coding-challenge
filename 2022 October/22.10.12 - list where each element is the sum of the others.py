# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 16:48:37 2022

@author: abelw
"""

import numpy as np

def element_mult(input_list):
    master_clone = list(input_list)
    output_list = []
    for element in input_list:
        local_clone = list(input_list)
        local_clone.remove(element)
        local_value = 1
        for element in local_clone:
            local_value *= element
        #print(local_value)
        output_list.append(int(local_value))
    return(output_list)
        

        
test_list = [3,2,1]
daily = element_mult(test_list)