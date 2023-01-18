""""
Compute the running median of a sequence of numbers. 
That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
2
1.5
2
3.5
2
2
2
"""

import math

def median_finder(sequence):
    sorted = [] #Define empty "sorted" list
    for element in sequence:
        #For element in input, appends to sorted and sorts
        sorted.append(element)
        sorted.sort()

        #Single element
        if len(sorted) == 1:
            print(sorted[0]) 
            #If single element, list - outputs that element

        #Odd number of elements
        elif (len(sorted) % 2) == 1:
            #Find middle element
            index = int((len(sorted)-1)/2)
            #Output middle element
            print(sorted[index])

        #Even number of elements
        elif (len(sorted) % 2) == 0:
            #Find middle 2 elements
            index_a, index_b = int(math.floor((len(sorted)-1)/2)), int(math.ceil((len(sorted)-1)/2))
            element_a = sorted[index_a]
            element_b = sorted[index_b]
            #Output average of 2 middle elements
            print(str((element_a + element_b)/2))

median_finder([2, 1, 5, 7, 2, 0, 5])
