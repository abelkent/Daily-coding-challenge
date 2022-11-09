# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 14:43:15 2022

Write an algorithm to justify text. Given a sequence of words and an integer 
line length k, return a list of strings which represents each line, fully 
justified.

More specifically, you should have as many words as possible in each line. 
There should be at least one space between each word. Pad extra spaces when 
necessary so that each line has exactly length k. Spaces should be distributed 
as equally as possible, with the extra spaces, if any, distributed starting 
from the left.

If you can only fit one word on a line, then you should pad the right-hand 
side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words
["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] 
and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly

@author: abelw
"""
import math

def justifier(sequence, k):
    output = []
    line= []
    line_length = 0
    
    for word in sequence:
        #Find maximum number of words per line
        if line_length + len(word) < k:
            line.append(word)
            line_length += len(word)
            print("Added "+word)
            
        else:
            print(line)
            next_line = []
            next_line.append(word)
            next_line_length = len(word)
            #Find spaces between each word
            gap = k - line_length
            spaces_per_word = math.floor(gap / (len(line) -1))
            #print(spaces_per_word)
            word_spaces = " "*spaces_per_word
            
            #Is there a remainder?
            if spaces_per_word != (gap / (len(line) -1)):
                first_space = " "*(spaces_per_word+1)
            else:
                first_space = word_spaces
            
            justified_line = ""
            justified_line += line[0] + first_space
            for index in range(1, len(line)-1):
                justified_line += line[index] + word_spaces
            justified_line += line[-1]
            output.append(justified_line)
            line = []
            line_length = 0
            
            line = next_line
            line_length = next_line_length
            

    
    return(output)

    #Pad remaining characters

test = justifier(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] , 16)
