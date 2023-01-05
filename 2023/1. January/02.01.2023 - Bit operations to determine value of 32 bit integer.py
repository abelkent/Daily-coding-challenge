"""
Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0,
using only mathematical or bit operations. You can assume b can only be 1 or 0

AKA, ¬(B)Y OR BX
"""

x = "10000110010011110110110001100110"
y = "11001101111111000001100010010110"
b = "00000000000000000000000000000000"

#Can make this more efficient, act on each input as a full register rather than each bit sequentially
def integer_comparison(x,y,b):

    #Defines output value and converts b into a single digit for bitwise operations
    output = ""
    digit_b = bool(int(b[0]))

    #For each digit in the inputs...
    for digit_x, digit_y in zip(list(x),list(y)):
        
        #...converts to appropriate format (bool)
        digit_x = bool(int(digit_x))
        digit_y = bool(int(digit_y))

        #Generates each operand
        operand_a = not(digit_b) and digit_y
        operand_b = digit_b and digit_x

        #Produces output
        output_digit = operand_a or operand_b
        output_digit = str(int(output_digit))

        #Converts back to string format and appends to output
        output = output+output_digit

    #Returns output
    return(output)



print(integer_comparison(x,y,b))