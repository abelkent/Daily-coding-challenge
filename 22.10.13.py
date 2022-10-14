# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 12:36:26 2022

@author: abelw
"""

def Node():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
node = Node('root', Node('left',
                         Node('left.left')),
            Node('right'))

