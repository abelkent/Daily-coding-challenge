"""
Implement 3 stacks using a single list:

class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        pass

    def push(self, item, stack_number):
        pass
"""


#Initially tried to do 1D array implementation, will try with 2D first (albeit a slightly cheaty one)

#2D implementation

class Stack_2D:
    def __init__(self):
        self.list = [[],[],[]]

    def pop(self, stack_number):
        return self.list[stack_number].pop(0)

    def push(self, item, stack_number):
        stack_get = self.list[stack_number]
        stack_get.insert(0, item)
        self.list[stack_number] = stack_get

stack = Stack_2D()
stack.push(1,0)
stack.push(2,1)
stack.push(3,2)

print(stack.pop(1))

#NOTE: 1D implementation
"""class Stack:
    def __init__(self):
        self.list = [None, None]
        self.stack_1_begin, self.stack_1_end = int(0)
        self.stack_2_begin, self.stack_2_end = int(1)
        self.stack_3_begin, self.stack_3_end = len(self.list)

    def pop(self, stack_number):
        pass

    def push(self, item, stack_number):
        pass

test = list([None, None])
test.insert(4,5)
print(test)
test.insert(1,2)
print(test)"""