"""
Given a list, sort it using this method: reverse(lst, i, j), which reverses lst from i to j.
"""

test_list = [0,1,2,3,4,5,6,7,8,9]

def reverse(lst, i, j):
    scope = len(lst)
    slice = lst[i:j+1]
    slice.reverse()
    #print(slice)
    for index in range(scope):
        if index in range(i, j+1):
            lst[index] = slice.pop(0)
    
    print(lst)

reverse(test_list, 2, 4)
reverse(test_list, 0,9)
