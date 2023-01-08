"""
Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).
"""

import random

n = 10
l = [1,3,5,7,9]


def exclusive_generator(n,l):
    #Loops until broken
    while True:
        #Generates random number
        generated = random.randint(0, n-1)
        #If number is not in l, returns number
        if generated not in l:
            return generated
#Notes: extremely compact - however has possibilty to endlessly generate invalid numebers (however minute)
#Could be updated to generate a list of valid numbers and then select a random entry from this list
#This would increase time and space complexity but negate the above mentioned possibility


#Definition of function to check uniform probability generation
def uniform_check():

    score_dict = dict()

    for i in range(10000):
        number = exclusive_generator(n,l)
        if number not in score_dict.keys():
            score_dict[number] = 1
        else:
            score_dict[number] += 1

    print(score_dict)

#uniform_check()
#Repeatedly generated results of approx. even probabilty for each valid output, no invalid outputs generated