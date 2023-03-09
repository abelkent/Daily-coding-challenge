"""
Given a binary tree where all nodes are either 0 or 1, prune the tree so that subtrees containing all 0s are removed.

For example, given the following tree:

   0
  / \
 1   0
    / \
   1   0
  / \
 0   0
should be pruned to:

   0
  / \
 1   0
    /
   1
We do not remove the tree at the root or its left child because it still has a 1 as a descendant.
"""

#Node class definitioon
class Node:
    def __init__(self, root, left = None, right = None):
        self.root = root
        self.left = left
        self.right = right
    
    #Function to check if subtree (including self) are comprised of all zero nodes
    def check_if_all_zero(self):

        if self.root == 0:
            root_value = True
        else:
            root_value = False
        
        if self.left == None:
            left_value = True
        else:
            left_value = self.left.check_if_all_zero()
    
        if self.right == None:
            right_value = True
        else:
            right_value = self.right.check_if_all_zero()
        
        return (root_value and left_value and right_value)

    #Pruning function that deletes child notes if they are all zero subtrees
    def prune(self):
        
        if self.left == None:
            pass
        elif self.left.check_if_all_zero() == True:
            self.left = None
        else:
            self.left.prune()
        
        if self.right == None:
            pass
        elif self.right.check_if_all_zero() == True:
            self.right = None
        else:
            self.right.prune()

test_node = Node(1,Node(0, Node(0)))
print(test_node.check_if_all_zero())
print(test_node.left.check_if_all_zero())
print(test_node.left.root)
test_node.prune()
#print(test_node.left.root) //Generates error as node no longer exists