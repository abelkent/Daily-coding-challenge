"""
Given a real number n, find the square root of n. For example, given n = 9, return 3.
"""

import math

def sqrt_cheatsy(n):
    #Uses Python's math library to cheese the answer
    return math.sqrt(n)


#Let's see if I can homebrew it
def sqrt_own(n):

    x = int(n)
    if x == n:
        print("Valid")
    else:
        print("Invalid")


sqrt_own(5)

#RETURN TO THIS
