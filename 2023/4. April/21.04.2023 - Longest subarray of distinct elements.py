"""
Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].
"""

example_array = [5, 1, 3, 5, 2, 3, 4, 1]

def subarray_finder(array):
    
    #Initialises empty lists for maximum and current local subarray
    maximum_array = list()
    local_subarray = list()
    
    #Iterates through all elements of input array
    for element in array:
        #Appends each element to local_subarray
        local_subarray.append(element)
        
        #Generates set of local_subarray for purposes of duplicate detection
        local_subset = set(local_subarray)
        #If a duplicate element is present (as detected by difference in set and array length difference) checks if local is greater than maximum and supplants it if True
        if len(local_subarray) != len(local_subset):
            if len(maximum_array) < len(local_subarray):
                maximum_array = local_subarray
            
            #While a duplicate is present in array, pops off first element until no longer True
            while True:
                local_subarray.pop(0)
                local_subset = set(local_subarray)
                
                if len(local_subarray) == len(local_subset):
                    break
    
    #Returns maximum subarray
    return maximum_array

print(subarray_finder(example_array))