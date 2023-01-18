# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 16:48:56 2022

The edit distance between two strings refers to the minimum number of character
 insertions, deletions, and substitutions required to change one string to the
 other. For example, the edit distance between “kitten” and “sitting” is three:
     substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.

@author: abelw
"""

def edit_distance_calc(string_a, string_b):
    
    #Enforce string_a as shortest
    if len(string_b) < len(string_a):
        string_a, string_b = string_b, string_a
    
    #Converts strings to lists
    string_a = [x for x in string_a]
    string_b = [x for x in string_b]
    
    #Finds initial distance as absolute difference in length between the 2
    distance = (abs(len(string_b) - len(string_a)))
    
    #Iterates through indexes in len(string_a) {the smaller of the 2 strings}
    for index in range(len(string_a)):
        #If the corresponding character in b doesn't match, increment distance by 1
        if string_a[index] != string_b[index]:
            distance+= 1
    
    #Return distance
    return(distance)
    
    
    

test = edit_distance_calc("kitten", "sitting")
