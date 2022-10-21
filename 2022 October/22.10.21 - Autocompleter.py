# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 16:37:41 2022

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

@author: abelw
"""

def autocomplete(s,queries,index=0):
    #print(queries)
    if index == len(s):
        return queries
    else:
        new_queries = []
        for word in queries:
            if s[index] == word[index]:
                new_queries.append(word)
        
        return(autocomplete(s,new_queries, index + 1))
    

test = autocomplete("de",["dog", "deer", "deal"])