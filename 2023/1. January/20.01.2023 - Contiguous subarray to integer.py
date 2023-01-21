"""
Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
"""

def contiguous_sum_finder(array, target):

    output_array = list()

    for element in array:
        output_array.append(element)
        if sum(output_array) > target:
            while sum(output_array) > target:
                output_array.pop(0)
        
        if sum(output_array) == target:
            print(output_array)
            return output_array
    


contiguous_sum_finder([1, 2, 3, 4, 5], 9)
