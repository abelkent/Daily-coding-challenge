"""
Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, 
which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.
"""

#Definition of function to check if a number is even (for later use)
def is_even(x):
    return (x%2 == 0)


def palindrome_permutation_check(word):

    word = list(word)
    letter_dict = dict()
    #Builds dict of letter occurences in word
    for letter in word:
        if letter not in letter_dict.keys():
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    
    #Retrieves number of occurences of letters
    letter_population = list(letter_dict.values())

    #Counts number of odd number counts of letters
    odds = int(0)
    for count in letter_population:
        if not is_even(count):
            odds += 1
    
    #If no odd letters, return True
    if odds == 0:
        return True
    #If 1 occurence of an odd letter, and length of word is not even, return True
    elif ((odds == 1) and not(is_even(len(word)))):
        return True
    #Otherwise return False
    else:
        return False
    
print(palindrome_permutation_check("carrace"))
print(palindrome_permutation_check("daily"))

