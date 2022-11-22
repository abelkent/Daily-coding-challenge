""""
Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. 
    If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. 
    If there are no elements in the stack, then it should throw an error or return null.
"""

class Stack(): #Class definition
    def __init__(self, data = list()): #Defines data default as empty list
        self.data = data
    
    def push(self, val):
        self.data.append(val) #Pushes value onto stack
    
    def pop(self):
        if len(self.data) == 0:
            return None #If len of stack is equal to zero, return None
        else:
            return self.data.pop() #Otherwise pop off last value and return
    
    def max(self):
        if len(self.data) == 0: #If len of stack is equal to zero, return None
            return None
        else:
            return max(self.data) #Otherwise return maximum value in stack

#Tests
"""test = Stack([1,2,3,4,5])
print(test.data)
test.pop()
print(test.data)
test.push(6)
print(test.max())"""