"""
This problem was asked by MongoDB.

Given a list of elements, find the majority element, which appears more than half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1.
"""

def majority_finder(array):

    element_dict = dict()
    for element in array:
        if element in element_dict.keys():
            element_dict[element] += 1

        else:
            element_dict[element] = int(1)

    print(element_dict)

    largest = int(0)
    output = None
    
    for element in element_dict.keys():
        if element_dict.get(element) > largest:
            output = element
            largest = element_dict.get(element)
    
    print(output)
    return output


majority_finder([1, 2, 1, 1, 3, 4, 0])