"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

def longest_consecutive_chain(array):
    current_chain_length = int(0)
    longest_chain_length = int(0)

    for index in range(1, len(array)):
        previous = array[index-1]
        current = array[index]

        print(previous, current)
    
        if current > previous:
            current_chain_length += 1
        else:
            current_chain_length = 0
        
        if current_chain_length > longest_chain_length:
            longest_chain_length = current_chain_length
    
    print(longest_chain_length)

longest_consecutive_chain([100, 4, 200, 1, 3, 2])