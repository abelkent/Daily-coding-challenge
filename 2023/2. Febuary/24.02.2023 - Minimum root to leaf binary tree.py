"""
Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

  10
 /  \
5    5
 \     \
   2    1
       /
     -1
"""

import math

class Node():
    def __init__(self, root, left = None, right = None):
        self.root = root
        self.left = left
        self.right = right


example_tree = Node(10, Node(5, None, Node(2)), Node(5,None, Node(1, Node(-1))))

def minimum_leaf_path_finder(tree, total = int(0)):

    new_total = total+tree.root

    if (tree.left == None) and (tree.right == None):
        return new_total

    if (tree.left == None):
        left_value = math.inf
    else:
        left_value = minimum_leaf_path_finder(tree.left, new_total)

    if (tree.right == None):
        right_value = math.inf
    else:
        right_value = minimum_leaf_path_finder(tree.right, new_total)
    
    return min(left_value, right_value)


print(minimum_leaf_path_finder(example_tree))

    
