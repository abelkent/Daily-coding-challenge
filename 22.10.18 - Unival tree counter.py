# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 16:34:22 2022

@author: abelw
"""

#Node class definition
class Node():
    def __init__(self, root, left = None, right = None):
        self.root = root
        self.left = left
        self.right = right
        
def unival_subtree_count(tree):
    
    if (tree.left == None) and (tree.right == None):
        return 1
    else:
        left_digit = "#"
        right_digit = "#"
        
        #Left node consideration
        if tree.left == None:
            left_score = 0
        else:
            left_score = unival_subtree_count(tree.left)
            left_digit = tree.left.root
        
        #Right node consideration
        if tree.right == None:
            right_score = 0
        else:
            right_score = unival_subtree_count(tree.right)
            right_digit = tree.right.root
        
        #Left and right node comparison
        if left_digit == right_digit:
            node_score = 1
        else:
            node_score = 0
        
        #Return
        return node_score + left_score + right_score
            
        

test = Node(1, Node(1), Node(0))

example = Node(0,
               Node(1),
               Node(0,
                    Node(1,
                         Node(1),
                         Node(1)),
                    Node(0)))

test_2 = unival_subtree_count(test)

