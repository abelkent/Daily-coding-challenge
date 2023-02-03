"""
Given an unsigned 8-bit integer, swap its even and odd bits. 
The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001.

Bonus: Can you do this in one line?
"""

def bit_swapper(eight_bit):

    eight_bit = list(eight_bit)

    for index in range(0,8,2):
        print(index)

print(bit_swapper("01010101"))

#UNFINISHED, GOT DISTRACTED, WILL COME BACK
