# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 15:34:59 2022

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), 
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

@author: abelw
"""

def minimum_room_finding(array):
    max_overlaps = 0
    for lesson in array:
        new_array =  list(array)
        new_array.remove(lesson)
        local_overlap = 0
        print(new_array)
        for check in new_array:
            if (check[0] in range(lesson[0], lesson[1])) or (check[1] in range(lesson[0],lesson[1])):
                local_overlap+=1
                print(local_overlap)
            
        #print(local_overlap)
        print(max_overlaps)
        
        if local_overlap > max_overlaps:
            max_overlaps = local_overlap

    
    if max_overlaps == 0:
        return 1
    else:
        return max_overlaps
        

example = [(30, 75), (0, 50), (60, 150)]
no_overlap = [(0,10),(11,20),(21,30)]
all_overlap = [(0,100),(20,80),(40,60),(45,55)]

test = minimum_room_finding(all_overlap)