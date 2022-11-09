# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 14:08:23 2022

Run-length encoding is a fast and simple method of encoding strings. 
The basic idea is to represent repeated successive characters as a single count
 and character. For example, the string "AAAABBBCCDAA" would be encoded as 
 "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be 
encoded have no digits and consists solely of alphabetic characters. 
You can assume the string to be decoded is valid.

@author: abelw
"""

def encoder(string):
    
    current_character = string[0] #Initialises current_character as first chracter
    current_count = 0 #Initialises current_count as 0
    output_string = "" #Initialises blank output string
    for character in string: #Iterates through all characters in input
        if character == current_character:
            current_count+=1 #Increments current_count by 1 if character matches current character
        else:
            output_string += str(current_count) + current_character #Adds character data to output string if not
            current_count = 1 #Resets current_count to 1
            current_character = character #Changes current_character to match new character
    
    output_string += str(current_count) + current_character #Adds final character data to output string
    
    return(output_string) #Returns output string

input_string = "AAAABBBCCDAA"

test = encoder(input_string)

def naive_decoder(sequence): #Functions but only with character counts < 10
    output_string = ""
    for index in range(0, len(sequence)-1,2):
        output_string += sequence[index+1] * int(sequence[index])
    return(output_string)

def decoder(sequence): #Functions for any value of int
    current_val = str() #Initialises current_val, current_char and output_string as strings
    current_char = str()
    output_string = str()
    
    #Iterates through index of sequence characters
    for index in range(len(sequence)):
        try:
            int(sequence[index]) #Try to convert character to int
        except:
            current_char = sequence[index] #If invalid (ie, is char rather than int) adds data to output string
            output_string += current_char * int(current_val)
            current_val = str() #Resets current_val
        else:
            current_val += sequence[index] #If valid (is int) adds number to current_val

    return output_string #Returns output string
        
test_2 = decoder(encoder(input_string))

print(test_2 == input_string)