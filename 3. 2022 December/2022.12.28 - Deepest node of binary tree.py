
"""
Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.
"""

class Node():
    #Initialisation
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    #Defines get deepest function
    def get_deepest(self, depth = 1):

        #Defines data variables for each branch of a single node
        self_data = [self.value, depth]
        
        if self.left == None:
            left_data = [None,0]
        else:
            left_data = self.left.get_deepest(depth+1)
        
        if self.right == None:
            right_data = [None, 0]
        else:
            right_data = self.right.get_deepest(depth+1)
        
        #Returns deepest node (weighted towards left)
        if (self_data[1] >= left_data[1]) and (self_data[1] >= right_data[1]):
            return self_data
        
        if (left_data[1] >= self_data[1]) and (left_data[1] >= right_data[1]):
            return left_data
        
        if (right_data[1] >= self_data[1]) and (right_data[1] >= left_data[1]):
            return right_data

test_node = Node("a", Node("b"), Node("c", Node("d")))

print(test_node.get_deepest())