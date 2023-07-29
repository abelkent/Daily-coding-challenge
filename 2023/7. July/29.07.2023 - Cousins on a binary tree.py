"""
Two nodes on a binary tree can be called "cousins" if they are on the same level of the binary tree but do not have the same parent.

Given a binary tree and a particular node, find all cousins of that node.
"""

class Node():
    def __init__(self, root, left = None, right = None):
        self.root = root
        self.left = left
        self.right = right


def cousin_locator(tree, node):

    def data_harvester(tree, target_node, depth = int(0), parent = None):
        
        if tree.root == target_node:
            return (depth, parent)
        
        if tree.left != None:
            left_value = data_harvester(tree.left, target_node)
        else:
            left_value = (int(0), int(0))
        
        if tree.right != None:
            right_value = data_harvester(tree.right, target_node)
        else:
            right_value = (int(0), int(0))
        
        new_depth = depth =+ 1
        new_parent = tree.root

        return max(left_value, right_value)

    print(data_harvester(tree, node))

test_tree = Node(1,Node(2, Node(4), Node(5)), Node(3, None,Node(6)))
test_node = 4

cousin_locator(test_tree, test_node)
 
