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

def justifier_OLD(sequence, k):
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


def justifier(sequence, k):
    all_lines = list()
    local_line = list()
    line_length = 0
    for word in sequence:
        word_length = len(word)
        if len(local_line) <= 1:
            abs_length = int(line_length)
        else:
            abs_length = line_length + (len(local_line) -1)
        #print(abs_length)
        if (abs_length + word_length) <= k:
            local_line.append(word)
            line_length += word_length
        else:
            all_lines.append(local_line)
            local_line = list()
            local_line.append(word)
            line_length = word_length
    
    if len(local_line) != 0:
        all_lines.append(local_line)
    
    
    for line in all_lines:
        line_length = sum([len(x) for x in line])
        padding = k - line_length
        
        spacing = padding // (len(line)-1)
        remainder = padding % (len(line)-1)
        #print(padding, spacing, remainder)

        justified_line = ""
        justified_line += line[0] + (" "*spacing) + (" "*remainder)
        for word in line[1:-1]:
            justified_line += word + (" "*spacing)
        justified_line += line[-1]

        print(justified_line, len(justified_line))

test = justifier(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] , 16)
print(test)