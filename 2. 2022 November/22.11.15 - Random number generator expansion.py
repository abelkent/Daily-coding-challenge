""""
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, 
implement a function rand7() that returns an integer from 1 to 7 (inclusive).
"""
#Import random number generator module
import random

def rand5():
    return random.randint(1,5)


#Distribution is wack,
#50% chance of 1-5
#50% chance 2 - 7 (skewed towards higher numbers)
def rand7():
    
    #Randomly decide if number will range from 1 -5 or 1 -7
    if random.randint(1,2) == 1:
        return rand5() #Return random number in range(1,5)
    
    else:
        while True:
            #Otherwise generate 2 random numbers in range(1,5)
            first_number = rand5()
            second_number = rand5()
            
            #If sum of numbers is less than or equal to 7, return to user, otherwise loop
            if first_number + second_number <= 7:
                return (first_number + second_number)
                
