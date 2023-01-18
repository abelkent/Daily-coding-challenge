# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 15:11:20 2022

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. 
If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

@author: abelw
"""

def deterministic_sentence_retriever(sentence, dictionary):
    local_string = str()
    output = list()
    for character in sentence:
        local_string += character
        if local_string in dictionary:
            output.append(local_string)
            local_string = ""
    
    if len(output) == 0:
        return None
    else:
        return output
 
def nondeterministic_setence_retriever(sentence, dictionary):           
    outputs = list()
    
    #Build up string until word is found
    #If word is part of a larger word, check if valid in sentence
        #If valid: return both
        #If not valid: return single
    
    
sentence_a = "thequickbrownfox"
dictionary_a = ['quick', 'brown', 'the', 'fox']

sentence_b = "bedbathandbeyond"
dictionary_b = ['bed', 'bath', 'bedbath', 'and', 'beyond']

#test = deterministic_sentence_retriever(sentence_b, dictionary_b)