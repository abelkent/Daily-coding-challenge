"""
Implement division of two positive integers without using the division, multiplication, or modulus operators.

Return the quotient as an integer, ignoring the remainder.
"""

def positive_division():

    #Recieves numerator and denominator as integer inputs from user (assumes correct format)
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    #Initialises zeroed output and current count
    output = int(0)
    count = int(0)

    #Loops (until broken = answer found)
    while True:
        #If current count is equal to numerator, breaks loop
        if count == numerator:
            break
        #If current count is greater than numerator, decrements output by 1 and breaks loop
        if count > numerator:
            output -= 1
            break

        #Increments count by denominator and output by 1 for each loop
        count += denominator
        output += 1

    #Outputs answer
    print(str(numerator) + "/" + str(denominator) + " = "+ str(output))

positive_division()