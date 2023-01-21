"""
Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
"""

def contiguous_sum_finder(array, target):

    #Initialises output array 
    output_array = list()

    #Iterates through elements in array, adding them to output array
    for element in array:
        output_array.append(element)
        #If sum of total list is greater than target, removes first element repeatedly until no longer satisfied
        while sum(output_array) > target:
            output_array.pop(0)
        
        #If sum of elements is equal to target, prints and returns list
        if sum(output_array) == target:
            print(output_array)
            return output_array
    


contiguous_sum_finder([1, 2, 3, 4, 5], 9)
