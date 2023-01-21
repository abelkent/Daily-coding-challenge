"""
Given a string and a set of characters, return the shortest substring containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, return null.
"""

def smallest_substring_locator(string, array):

    shortest_substring = str(string)
    current_substring = str()

    def substring_satisfies(substring):
        outputs = list()

        for character in array:
            outputs.append(character in substring)

        return not(False in outputs)
    
    #print(substring_satisfies("abdd"))

    for starting_index in range(len(string)):
        starting_character = string[starting_index]

        if starting_character in array:
            #Begin adding other letters to current substring

            current_substring = starting_character
            
            for following_index in range(starting_index+1, len(string)):
                following_character = string[following_index]
                current_substring += following_character

                if substring_satisfies(current_substring):
                    if current_substring < shortest_substring:
                        shortest_substring = current_substring
                        current_substring = ""
                        print("NEW SHORTEST SUBSTRING :"+ shortest_substring)

                    else:
                        print("RESET")
                        current_substring = ""
        
    print (shortest_substring)


smallest_substring_locator("figehaeci",["a","e","i"])



def smallest_substring_locator_OLD(string, array): #Doesn't work

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
                        current_substring = str()
                    if len(current_substring) < len(shortest_substring):
                        shortest_substring = current_substring
                        current_substring = str()
        
    print (shortest_substring)


#smallest_substring_locator_OLD("figehaeci",["a", "e", "i"])

