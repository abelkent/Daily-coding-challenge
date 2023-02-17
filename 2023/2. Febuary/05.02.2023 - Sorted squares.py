"""
Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
"""

#Function definition
def square_sorter(array):
    #Array set to the square of elements
    array = [(x)**2 for x in array]
    #Array is sorted
    array.sort()
    #Array is printed
    print(array)

square_sorter([-9, -2, 0, 2, 3])