# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 12:36:26 2022

@author: abelw
"""

class Node():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
node = Node('root', Node('left',
                         Node('left.left')),
            Node('right'))

test_node = Node("root", Node("left"))

def serialise(node):
    
    #Has no children
    if (node.left == None) and (node.right == None):
        return (node.val + " " + "#" + " " + "#")
    
    #Has left child
    elif (node.left != None) and (node.right == None):
        return (node.val + " " + serialise(node.left) +" "+ "#")
    
    #Has right child
    elif (node.left == None) and (node.right != None):
        return (node.val + " " + "#" + " " +serialise(node.right))
    
    #Has both children
    elif (node.left != None) and (node.right != None):
        return (node.val + " " + serialise(node.left) + " " + serialise(node.right))

test_serial = serialise(test_node)
experimental_serial = serialise(node)

example_node = Node("1", 
                    Node("2",
                         Node("4"),
                         Node("5")),
                    Node("3",
                         right = Node("6")))

example_serial = serialise(example_node)

def deserialise(s):
    node_list = s.split(" ")
    iterable_nodes = iter(node_list)
    
    def recursion_function():
        
        root = next(iterable_nodes) #Get next node, assign as root
        if root == "#": #If root is # return None
            return None
        else: #Else return recursion_function output of next 2 characters
            return Node(root, recursion_function(), recursion_function())
    
        
    return recursion_function()
    
    #Right tree

test = deserialise(test_serial)
example = deserialise(example_serial)

    
    
    
