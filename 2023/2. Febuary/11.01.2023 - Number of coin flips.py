"""
You have n fair coins and you flip them all at the same time. Any that come up tails you set aside. The ones that come up heads you flip again. How many rounds do you expect to play before only one coin remains?

Write a function that, given n, returns the number of rounds you'd expect to play until one coin remains.

Notes:
2/2 = 1
4/2/2 = 1
8/2/2/2 = 1
16/2/2/2/2 = 1

2 = 2^1
4 = 2^2
8 = 2^3
16 = 2^4

Returns powers of 2 of number

In between range?
3/2 round up = 2, 2/2 = 1 (2)

7/2 round up = 4, 4/2 = 2, 2/2 = 1 (3)

13/2 round up = 7, 7/2 round up = 4, 4/2 = 2, 2/2 = 1 (4)
15/2 round up = 8, 8/2 = 4, 4/2 = 2, 2/2 = 1 (4)

Returns next highest power of 2.
"""

def coin_flip_eliminator(n):

    #Initialisers power as 0
    power = int(0)

    #While 2 to the power of power is less than n incremements power
    while (2**power < n):
        power +=1

    #Prints and returns power when it is >= n
    print(power)    
    return power

coin_flip_eliminator(4)

