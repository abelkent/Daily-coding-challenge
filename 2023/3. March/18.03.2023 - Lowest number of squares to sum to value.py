"""
Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 32 + 22 = 9 + 4.

Given n = 27, return 3 since 27 = 32 + 32 + 32 = 9 + 9 + 9.
"""

import math

def check_if_square(x):
    return math.sqrt(x).is_integer()


def square_sum_finder(n, total = int(0)):
    
    if n == int(0):
        return total
    
    else:
        for step in range(n, 0, -1):
            if check_if_square(step):
                return (square_sum_finder(n - step, total + 1))

    


#def smallest_square_sums(n):

