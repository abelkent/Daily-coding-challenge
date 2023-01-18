"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

#Function definition
def longest_consecutive_chain(array):

    #Defines hash and n as the set and length of input array respectively
    hash = set(array)
    n = len(array)

    #Longest and current chain initialised at zero
    longest_chain = int(0)
    current_chain = int(0)
    
    #For index in range n...
    for i in range(n):
        #If the previous element is NOT in hash (ie, is the start of a chain, even if only a chain of 1)...
        if array[i]-1 not in hash:
            #Chain length is updated
            current_chain = 1
            #Current lement is initialised
            current_element = array[i]
            #While the following element is in hash (ie, the sequence continues)...
            while (current_element + 1) in hash:
                #Chain length and current element is updated is updated
                current_chain += 1
                current_element += 1
            
            #longesst chain is set as the maximum value of the 2 values
            longest_chain = max(current_element, current_chain)
    
    #Outputs longest chain value
    print(longest_chain)

longest_consecutive_chain([100,4,200, 1, 3, 2])
    