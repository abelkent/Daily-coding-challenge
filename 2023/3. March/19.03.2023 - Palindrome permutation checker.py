"""
Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, 
which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.
"""

def is_even(x):
    return (x%2 == 0)


def palindrome_permutation_check(word):
    word = list(word)
    letter_dict = dict()
    for letter in word:
        if letter not in letter_dict.keys():
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    
    letter_population = list(letter_dict.values())

    odds = int(0)
    for count in letter_population:
        if not is_even(count):
            odds += 1
    
    if odds == 0:
        return True
    elif ((odds >= 1) and (is_even(len(word)))):
        return True
    elif ((odds == 1) and not(is_even(len(word)))):
        return True
    else:
        return False
    
print(palindrome_permutation_check("carrace"))
print(palindrome_permutation_check("daily"))

