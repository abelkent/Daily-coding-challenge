"""
Given a string which we can delete at most k, return whether you can make a palindrome.

For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.
"""

def palindrome_checker(palindrome, k):

    invalid_character_count = int(0)

    palindrome, palindrome_clone = list(palindrome),list(palindrome)
    palindrome_clone.reverse()
    print(palindrome, palindrome_clone)

    halfway_point_reached = bool(False)
    
    index = int(0)

    for character in palindrome:
        
        print(character)
        print(palindrome_clone[index])
        index += 1




    
palindrome_checker("cat",2)