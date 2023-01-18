""""
Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. 
If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it 
(which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" 
by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
"""

import string

def palidrome_generator_OLD(sequence):

    #Gets alphabet
    alphabet = list(string.ascii_uppercase)
    #print(alphabet)

    #Determine if palindrome
    #Sets sequence to uppercase
    sequence = sequence.upper()
    sequence = [x for x in sequence]

    backwards_sequence = list(sequence)
    backwards_sequence.reverse()
    
    if backwards_sequence == sequence:
        return ("INPUT IS ALREADY A PALINDROME")
    

    def forward_vs_backwards(forwards, backwards):
        forward_index = alphabet.index(forwards[0])
        backward_index = alphabet.index(backwards[0])

        if forward_index < backward_index:
            return "Forward"
        
        elif forward_index > backward_index:
            return "Backwards"
        
        elif forward_index == backward_index:
            return forward_vs_backwards(forwards[1:], backwards[1:])

    direction = forward_vs_backwards(sequence, backwards_sequence)


    print(direction)

    if direction == "Forwards":
        index = 0
    elif direction == "Backwards":
        index = -1
    
    print(sequence[index])


def palindrome_generator(sequence):
    sequence = sequence.upper()
    sequence = [x for x in sequence]
    reverse = list(sequence)
    reverse.reverse()
    print(sequence, reverse)

palindrome_generator("cat")