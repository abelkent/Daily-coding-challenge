"""
Let's represent an integer in a linked list format by having each node represent a digit in the number. The nodes make up the number in reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5
is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

9 -> 9
5 -> 2
return 124 (99 + 25) as:

4 -> 2 -> 1
"""

class Node():
    def __init__(self, root, leaf = None):
        self.root = root
        self.leaf = leaf

def node_output(node):
    
    output = str()

    def recursive(link):

        nonlocal output
        output += str(link.root)

        if link.leaf != None:
            recursive(link.leaf)
    
    recursive(node)
    print(output)
    return int(output)


def node_genetator(number):

    number = list(number)
    
    new_node = Node(root = number[0])
    number.pop(0)
    print(number)

node_genetator(321)
def node_addition(node_a, node_b):
    node_a, node_b = node_output(node_a), node_output(node_b)
    node_total = node_a + node_b


#UNFINISHED


linked_number = Node(1, Node(2, Node(3)))
another_linked_number = Node(9, Node(5))

node_addition(linked_number, another_linked_number)