# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 16:37:44 2022

Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)

Do this in O(n) time and O(k) space. 
You can modify the input array in-place and you do not need to store the results. 
You can simply print them out as you compute them.

@author: abelw
"""

#Need to verify time complexity
def largest_value(array, k):
    sub_array = []*k
    for step in range(0,len(array)-(k-1)):
        print(max(array[step:step+k]))
        
        

x = [10, 5, 2, 7, 8, 7]
largest_value(x,3)
