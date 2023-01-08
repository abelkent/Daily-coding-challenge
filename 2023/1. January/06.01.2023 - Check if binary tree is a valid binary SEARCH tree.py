"""
A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key
in the left child must be less than or equal to the root and the key in the right child must be greater 
than or equal to the root.
"""

#Node class definition
class Node():

    #Init function
    def __init__(self, root, left = None, right = None):
        self.root = root
        self.left = left
        self.right = right

    #Recursive valid checker
    def check_if_valid_search_tree(self):

        #If left node is "None" is determined to be valid
        if (self.left == None):
            left_valid = True
        else:
            #Otherwise checks if left node is less than or equal to root, and if itself is valid
            if (self.left.root <= self.root) and (self.left.check_if_valid_search_tree() == True):
                left_valid = True
            else:
                left_valid = False
        
        #Repeats for right node
        if (self.right == None):
            right_valid = True
        else:
            if (self.right.root >= self.root) and (self.right.check_if_valid_search_tree() == True):
                right_valid = True
            else:
                right_valid = False
        

        #Returns if left and right nodes are valid
        return (left_valid == True) and (right_valid == True)



test_node = Node(3,Node(1), Node(4))

#print(test_node.right.check_if_valid_search_tree())
#print(test_node.left.check_if_valid_search_tree())
#print(test_node.right.check_if_valid_search_tree())
#print(test_node.left.root <= test_node.root)
#print(test_node.right.root >= test_node.root)
print(test_node.check_if_valid_search_tree())
