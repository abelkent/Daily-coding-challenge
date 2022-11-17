""""
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
"""

def power_set_generator(set):
    print(set)
    for item in set:
        print(item)

power_set_generator({1, 2, 3})