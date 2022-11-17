
""""
Given the root to a binary search tree, find the second largest node in the tree.
"""

class Node():
    def __init__(self, root, left = None, right = None):
        self.root = root
        self.left = left
        self.right = right

def second_largest_node(node):


    def retrieve_values(node):


        root_value = node.root

        if node.left == None:
            left_value = "#"
        else:
            left_value = retrieve_values(node.left)
        
        if node.right == None:
            right_value = "#"
        else:
            right_value = retrieve_values(node.right)

        return (str(root_value) + "-" + str(left_value) + "-" + str(right_value))
    
    
    def character_processing(sequence):
        sequence = sequence.split("-")
        while "#" in sequence:
            sequence.remove("#")
            #print(sequence)
        
        sequence = [int(x) for x in sequence]
        sequence.sort()
        return(sequence[1])
    
    return character_processing(retrieve_values(node))

test_tree = Node(1, Node(2, Node(3)))

print (second_largest_node(test_tree))