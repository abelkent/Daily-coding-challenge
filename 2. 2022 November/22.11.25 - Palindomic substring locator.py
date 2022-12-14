"""
Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".
"""

def palindromic_substring_locator(intake):
    #Defines empty list of palindromes
    longest_palindrome = []
    
    #Converts intake to list
    intake = [x for x in intake]
    
    #For each character in intake
    for index in range(len(intake)):
        local_string = [] #Defines empty "local_string"
        starting_character = intake[index] #Adds starting character to local_string
        local_string.append(starting_character)

        for step in range(index+1, len(intake)): #For each character between starting character and end of intake string...
            local_string.append(intake[step])
            invert = list(local_string)
            invert.reverse()
            #Adds to local_string and creates a reverse copy of it, if the two match (ie, is a palidrome) it is added to palindrome list
            
            if (local_string == invert) and (len(local_string) > len(longest_palindrome)):
                longest_palindrome = list(local_string)


    #If there are no palindromes present (1 string substrings are not considered) returns None
    if len(longest_palindrome) == 0:
        return None
    else: #Otherwise finds longest present palindrome
        return "".join(longest_palindrome)
print(palindromic_substring_locator("banana"))