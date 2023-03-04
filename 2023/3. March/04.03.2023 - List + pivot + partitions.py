"""
Given a pivot x, and a list lst, partition the list into three parts.

The first part contains all elements in lst that are less than x
The second part contains all elements in lst that are equal to x
The third part contains all elements in lst that are larger than x
Ordering within a part can be arbitrary.

For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14].
"""

#This question confused me for the fact that it seems to overcomplicating a sorting algorithm
#Ergo, here's one (cheatsy) implementation

"""def solution(lst, x):
    return sorted(lst)

print(solution([9, 12, 3, 5, 14, 10, 10],10))
"""

#MOVING ON

def pivot_sorter(array, pivot):
    #Initialises 3 empty partitions
    partition_1, partition_2, partition_3 = list(),list(), list()
    
    #Iterates through input array and places them in appropriate partition
    for element in array:
        if element < pivot:
            partition_1.append(element)
        elif element == pivot:
            partition_2.append(element)
        else:
            partition_3.append(element)

    #Returns concatenated partitions
    return (partition_1 + partition_2 + partition_3)

print(pivot_sorter([9, 12, 3, 5, 14, 10, 10],10))