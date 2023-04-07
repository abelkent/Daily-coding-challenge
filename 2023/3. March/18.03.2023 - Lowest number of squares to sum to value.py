"""
Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 32 + 22 = 9 + 4.

Given n = 27, return 3 since 27 = 32 + 32 + 32 = 9 + 9 + 9.
"""

#Imports math for later usage
import math

#Definition of function that returns if a value is a square number
def check_if_square(x):
    return math.sqrt(x).is_integer()



def square_sum_finder(n, total = int(0)):
    
    #If n is equal to 0, return total (default: 0)
    if n == int(0):
        return total
    
    #Otherwise iterate from n to zero checking if each value is square
    #If it is; return value of square_sum_finder with new value of n (n - step) and new total (+= 1)
    else:
        for step in range(n, 0, -1):
            if check_if_square(step):
                return (square_sum_finder(n - step, total + 1))

    

