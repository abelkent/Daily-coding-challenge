"""
Given a set of closed intervals, find the smallest set of numbers that covers all the intervals. 
If there are multiple smallest sets, return any of them.

For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers all these intervals is {3, 6}.
"""

import math

#OLD IMPLEMENTATION
"""def span_finder(intervals):
    interval_ranges = []

    lowest = math.inf
    highest = int(0)

    for interval in intervals:

        if interval[0] < lowest:
            lowest = interval[0]
        if interval[1] > highest:
            highest = interval[1]

        local_range = [x for x in range(interval[0],interval[1]+1)]
        interval_ranges.append(local_range)
    
    print(interval_ranges)
    print(lowest, highest)

    all_encompasing = [x for x in range(lowest, highest+1)]
    print(all_encompasing)

    #Upwards knockoff
    print(all(type(x) == float for x in local_range))


span_finder([[0, 3], [2, 6], [3, 4], [6, 9]])
"""

def span_finder(list_of_intervals):

    lowest_point = math.inf
    highest_point = int(0)

    for interval in list_of_intervals:
        print([x for x in range(interval[0], interval[1]+1)])
        if lowest_point > interval[0]:
            lowest_point = interval[0]
        if highest_point < interval[1]:
            highest_point = interval[1]
        
    
    print(lowest_point, highest_point)
    all_encompassing = [x for x in range(lowest_point, highest_point+1)]
    print(all_encompassing)

    upwards_check, downwards_check = False,False
    while not(upwards_check):

        for interval in list_of_intervals:

            new_sublist = list(all_encompassing)
            new_sublist.pop(0)

            span = [x for x in range(interval[0], interval[1]+1)]
            if all(x in new_sublist for x in span) == False:
                print("LOWEST POINT FOUND")
                print(all_encompassing)
                upwards_check = True
                
                
        all_encompassing = new_sublist
        print("NEW ALL ENCOMPASSING")
        print(all_encompassing)
    
    print(all_encompassing)

    while not(downwards_check):

        for interval in list_of_intervals:

            new_sublist = list(all_encompassing)
            new_sublist.pop()

            span = [x for x in range(interval[0], interval[1]+1)]
            
            if all(x in new_sublist for x in span) == False:
                print(span)
                downwards_check = True
            else:
                all_encompassing = new_sublist

    print(all_encompassing)
span_finder([[0, 3], [2, 6], [3, 4], [6, 9]])