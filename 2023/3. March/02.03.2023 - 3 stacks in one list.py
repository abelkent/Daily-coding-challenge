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

class Stack:
    def __init__(self):
        self.list = [None, None]
        self.stack_1_begin, self.stack_1_end = int(0)
        self.stack_2_begin, self.stack_2_end = int(2)
        self.stack_3_begin, self.stack_3_end = int(4)

    def pop(self, stack_number):
        pass

    def push(self, item, stack_number):
        pass