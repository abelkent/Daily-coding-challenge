"""
Given a list, sort it using this method: reverse(lst, i, j), which reverses lst from i to j.
"""

test_list = [0,1,2,3,4,5,6,7,8,9]

def reverse(lst, i, j):
    #Initialises "scope" as length of lst
    scope = len(lst)
    #Gets slice of list to be reversed within list and reverses it
    slice = lst[i:j+1]
    slice.reverse()
    #Iterates through list
    for index in range(scope):
        #If index of element is in range of i-j, replaces element with first element of slice (and removes it from slice)
        if index in range(i, j+1):
            lst[index] = slice.pop(0)
    
    #prints and returns lst
    print(lst)
    return lst

reverse(test_list, 2, 4)
reverse(test_list, 0,9)
