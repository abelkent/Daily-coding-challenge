# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 16:49:29 2022

Implement locking in a binary tree. 
A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

    - is_locked, which returns whether the node is locked
    - lock, which attempts to lock the node. 
    If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
    - unlock, which unlocks the node. If it cannot be unlocked, then it should return false. 
    Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you would like. 
You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. 
Each method should run in O(h), where h is the height of the tree.

@author: abelw
"""

class Lockable_Tree_Node():
    def __init__(self, root, left = None, right = None, locked = False):
        self.root = root
        self.left = left
        self.right = right
        self.locked = locked
        
    def is_locked(self):
        return self.locked
    
    def descendant_lock_state(self): #Returns lock state of all descendants
    #True = A descendant is locked, False = None of them are
        if self.left == None:
            left_locked = False
        else:
            left_locked = self.left.descendant_lock_state()
        
        if self.right == None:
            right_locked = False
        else:
            right_locked = self.right.descendant_lock_state()
        
        return (self.locked or left_locked or right_locked)
    
    def ancestors_lock_state(self, target):
        
        if self.root == None:
            return False
        
        if self.root == target:
            return self.locked
        
            
        

    def lock(self):
        if self.is_locked() == False:
            self.locked = True
        
        return self.locked
    
    def unlock(self):
        pass

test = Lockable_Tree_Node(1,
                          Lockable_Tree_Node(2, locked = True))
print(test.is_locked())
print(test.descendant_lock_state())
test.lock()
print(test.is_locked())