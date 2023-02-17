"""
Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.

For example, given the following tree and K of 20

    10
   /   \
 5      15
       /  \
     11    15
Return the nodes 5 and 15.
"""

class Node():
    def __init__(self, root, left = None, right = None):
        self.root = root
        self.left = left
        self.right = right


def target_node_finder(tree, target):

    all_nodes = list()

    def return_all_nodes(tree):

        all_nodes.append(tree.root)
        
        if tree.left == None:
            pass
        else:
            return_all_nodes(tree.left)
        
        if tree.right == None:
            pass
        else:
            return_all_nodes(tree.right)
    
    return_all_nodes(tree)
    

    def find_sum_to_target(array, target):

        for initial_value in array:
            array_clone = list(array)
            array_clone.remove(initial_value)

            for secondary_value in array_clone:
                if (initial_value + secondary_value) == target:
                    return (initial_value, secondary_value)
    
    print(find_sum_to_target(all_nodes, target))
        
    


tree = Node(1, Node(2), Node(3, Node(4)))
target_node_finder(tree, 4)