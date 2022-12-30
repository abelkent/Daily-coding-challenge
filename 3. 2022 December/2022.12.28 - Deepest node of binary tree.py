
"""
Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.
"""

class Node():
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def get_deepest(self, depth = 1):

        self_data = [self.value, depth]
        
        if self.left == None:
            left_data = [None,0]
        else:
            left_data = self.left.get_deepest(depth+1)
        
        if self.right == None:
            right_data = [None, 0]
        else:
            right_data = self.right.get_deepest(depth+1)
        
        if (self_data[1] >= left_data[1]) and (self_data[1] >= right_data[1]):
            return self_data
        
        if (left_data[1] >= self_data[1]) and (left_data[1] >= right_data[1]):
            return left_data
        
        if (right_data[1] >= self_data[1]) and (right_data[1] >= left_data[1]):
            return right_data

test_node = Node("a", Node("b"), Node("c", Node("d")))

print(test_node.get_deepest())