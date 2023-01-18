# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 17:00:31 2022

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

@author: abelw
"""

def longest_substring_locator(k, s):
    
    longest_substring = []
    local_string = []
    index = 0
    s = [x for x in s]
    print(s)
    
    while index < len(s):
        
        local_string.append(s[index])
        print(local_string)
        new_set = set(local_string)
        index = index+1
        
        if (len(local_string) > len(longest_substring)) and (len(new_set) <= k):
            longest_substring = list(local_string)
        
        elif (len(new_set)) > k:
            local_string = []
            index = index-2
    
    return (longest_substring)
        
    

test = longest_substring_locator(2,"abcba")
        