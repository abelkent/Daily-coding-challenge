"""
Given a string and a set of characters, return the shortest substring containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, return null.
"""

def smallest_substring_locator(string, array):

    shortest_substring = str()
    current_substring = str()

    for starting_index in range(len(string)):
        character = string[starting_index]

        def check_all_letters(substring):
            outputs = list()
            for character in array:
                outputs.append(character in substring)
            
            if False in outputs:
                return False
            else:
                return True
        
        if character in array:
            current_substring += character
            
            for secondary_index in range(starting_index+1, len(string)):
                current_substring += (string[secondary_index])

                check = check_all_letters(current_substring)
                if check == True:
                    if shortest_substring == "":
                        shortest_substring = current_substring
                    if len(current_substring) < len(shortest_substring):
                        shortest_substring = current_substring
        
    print (shortest_substring)


smallest_substring_locator("figehaeci",["a", "e", "i"])

