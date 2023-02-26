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

#Math library import for use of infinity function to represent infinitely large numbers
import math


#Node class definition
class Node():
    def __init__(self, root, left = None, right = None):
        self.root = root
        self.left = left
        self.right = right


#Example tree initialisation
example_tree = Node(10, Node(5, None, Node(2)), Node(5,None, Node(1, Node(-1))))

#Function definition
def minimum_leaf_path_finder(tree, total = int(0)):

    #Defines new total as provided total from parent node plus new node root
    new_total = total+tree.root

    #If has no children (is a leaf) returns new_total
    if (tree.left == None) and (tree.right == None):
        return new_total

    #If has no left child sets left value to infinitely large number, otherwise set as the recursive call of left side of given node
    if (tree.left == None):
        left_value = math.inf
    else:
        left_value = minimum_leaf_path_finder(tree.left, new_total)

    #If has no right child sets left value to infinitely large number, otherwise set as the recursive call of right side of given node
    if (tree.right == None):
        right_value = math.inf
    else:
        right_value = minimum_leaf_path_finder(tree.right, new_total)
    
    #Returns minimum of left/right child nodes
    return min(left_value, right_value)

#Call on example tree
print(minimum_leaf_path_finder(example_tree))

#NOTE: Does not return path to follow, just minimum sum total
    
