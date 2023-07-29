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

    def data_harvester(leaf, target_node, depth = int(0), parent = None):
        
        if tree.root == target_node:
            return (depth, parent)
        
        else:

            new_depth = depth =+ 1
            new_parent = tree.root

            return max(data_harvester(tree.left, target_node, new_depth, new_parent ))
        
        
