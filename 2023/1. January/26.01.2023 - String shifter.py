"""
Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
"""

def string_shifter(start_string, goal_string):

    #Convets input strings to list for easier manipulation
    start_string, goal_string = list(start_string), list(goal_string)

    #Sets max_shifts to length of initial string and current_shifts to zero
    max_shifts = len(start_string)
    current_shifts = int(0)

    #Checks if both strings are of same length
    if len(start_string) != len(goal_string):
        return False

    #While current shifts is not equal to max shifts (as this indicates entire string has been shifted), iterates the following:
    while current_shifts != max_shifts:

        #Shifted character is removed from end of start_string and inserted at the beginning
        shifted_character = start_string.pop()
        start_string.insert(0, shifted_character)
        
        #If start and goal are now equal, return True
        if start_string == goal_string:
            return True
        
        #Increment current shifts
        current_shifts += 1
    
    #Return False if condition is not met
    return False
        

    

print(string_shifter("abcde","cdeab"))

