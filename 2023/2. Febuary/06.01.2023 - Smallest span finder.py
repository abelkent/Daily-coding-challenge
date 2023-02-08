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

    list_of_ranges = list()
    for interval in list_of_intervals:
        if lowest_point > interval[0]:
            lowest_point = interval[0]
        if highest_point < interval[1]:
            highest_point = interval[1]
        
    
    #Count up
    starting_point_check = bool(False)
    starting_point = int(lowest_point)

    while not(starting_point_check):
        starting_point += 1

        for interval in list_of_intervals:
            if (starting_point > interval[0]) and (starting_point >= interval[1]):
                starting_point_check = True
                break
    
    ending_point_check = bool(False)
    ending_point = int(highest_point)

    while not(ending_point_check):
        ending_point -= 1

        for interval in list_of_intervals:
            if (ending_point < interval[1]) and (ending_point <= interval[0]):
                ending_point_check = True
                break

        
    print([starting_point, ending_point])
    return [starting_point, ending_point]
span_finder([[0, 3], [2, 6], [3, 4], [6, 9]])


#Useful utility function but realised I was overcomplicating my approach
"""    def common_element_check(subset, superset):
        return not all(x not in superset for x in subset)"""