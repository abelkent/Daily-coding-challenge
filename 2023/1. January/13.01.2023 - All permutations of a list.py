"""
Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
"""

import math
import itertools

"""
INVALID IMPLENTATION: GENERATES SLICES OF ARRAY UP TO FINAL ARRAY
def permutation_maker(array):

    def get_number_of_permutations(array):
        length = len(array)
        number_of_permutations = math.factorial(length)
        return number_of_permutations
    
    def get_all_permutations(array):

        list_of_permutations = list()
        
        def recursive_function(permutation, array):
            
            if len(array) == 0:
                return

            permutation_clone = list(permutation)
            permutation_clone.append(array[0])

            if permutation_clone not in list_of_permutations:
                list_of_permutations.append(permutation_clone)
            
            for character in array[1:]:
                recursive_function(permutation_clone, array[1:])
        

        recursive_function([],array)  
        print(list_of_permutations)  
    get_all_permutations(array)"""


#Prebuilt method

def itertools_implementation(array):
    
    return list(itertools.permutations(array))

#print(itertools_implementation([1,2,3]))

#Brute force method
import random
"""
THOUGHT THIS WOULD BE A FUN LITTLE TASK AND IT DOESN'T WORK, WHOOPSIE
def bruteforce_method(array):
    
    number_of_permutations = math.factorial(len(array))

    all_permutations = list()
    all_permutations.append(array)

    while len(all_permutations) != number_of_permutations:
        clone = random.shuffle(array)
        if clone not in all_permutations:
            all_permutations.append(clone)
    
    return(all_permutations)"""

print(5)
print(bruteforce_method([1,2,3]))
