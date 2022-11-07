# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:38:27 2022

@author: abelw
"""

def bracket_validator(sequence): #Accepts string of brackets as "sequence"

    #Defines dict of bracket pairs
    matching_pairs = {"(":")",
                          "[":"]",
                          "{":"}"}
    
    #Assigns key values to "opening_characters"
    opening_characters = matching_pairs.keys()
    
    stack = list()
    #Defines "stack" as an empty list
    for item in sequence: #Iterates through items in sequence
        if item in opening_characters: #If item is an opening bracket adds corresponding closing bracket to stack
            stack.append(matching_pairs[item]) 
        else: #If item is not an opening bracket
            final_character = stack.pop() #Pops final bracket (expected character) off of stack
            if final_character != item:
                return False #If item and final_character do not match, return False
    
    #After iteration checks if stack is empty, and returns True if yes and False if not
    if len(stack) != 0:
        return False
    else:    
        return True

test = bracket_validator("([)]")