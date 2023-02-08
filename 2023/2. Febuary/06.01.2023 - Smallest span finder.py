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

