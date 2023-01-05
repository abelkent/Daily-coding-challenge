"""
Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the string valid 
(i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we must remove all of them.
"""

def invalid_bracket_counter(sequence):

    #Initialises empty stack and zeroed error count
    stack = list()
    invalid_total = int(0)

    #Defines open and close bracket for readability
    open_bracket = "("
    close_bracket = ")"

    #Iterates through characters in sequence
    for character in sequence:
        #Adds close bracket to stack for each open bracket
        if character == open_bracket:
            stack.append(close_bracket)
        
        #For each valid close bracket, last item on stack is popped off
        elif (character == close_bracket) and (len(stack) > 0):
            stack.pop()
        
        #For each invalid close bracket, invalid count is incremented
        else:
            invalid_total += 1
        
    #Adds length of remaining stack to invalid total (number of invalid open brackets)
    invalid_total += len(stack)

    #Returns invalid total
    return (invalid_total)

print(invalid_bracket_counter(")("))