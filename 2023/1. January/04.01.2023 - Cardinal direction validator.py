"""
A rule looks like this:

A NE B

This means this means point A is located northeast of point B.

A SW C

means that point A is southwest of C.

Given a list of rules, check if the sum of the rules validate. For example:

A N B
B NE C
C N A

does not validate, since A cannot be both north and south of C.

A NW B
A N B

is considered valid.
"""

invalid_rule_list = ["A N B", "B NE C", "C N A"]
valid_rule_list = ["A NW B", "A N B"]

def rule_checker(list_of_rules):
    south_to_north = list()
    west_to_east = list()

    for rule in list of rules:
        rule = rule.split(" ")
        directions = rule[1]
        directions = [x for x in directions]
        origin = rule[0]
        destination = rule[-1]
        
    
    