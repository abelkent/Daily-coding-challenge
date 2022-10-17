# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 17:51:14 2022

@author: abelw
"""

def unique_decoding_count(numbers):
    
    def recursion(data):
        #print(data)
        #print(data)
        data_length = len(data)
        if data_length == 0:
            print("Reached base")
            return 0
        elif data_length == 1:
            print("Reached final: "+ str(data[0]))
            return 1
        else:
            double = int("".join((data[0],data[1])))
            #print(double)
            if double <= 26:
                print("Valid double: "+ str(double))
                #return("C")
                return (2 + recursion(data[1:]))
            else:
                print("Invalid double:"+str(double))
                return (1 + recursion(data[1:]))
        
    
    return(recursion(numbers))
            
            #includes 2


def take_2(encoding):
    
    if len(encoding) == 0:
        return 0
    elif len(encoding) == 1:
        return 1
    elif len(encoding) == 2:
        double = int("".join((encoding[0],encoding[1])))
        
        if double <= 26:
            return 2
        else:
            return 1
    else:
        double = int("".join((encoding[0],encoding[1])))
        
        if double <= 26:
            return take_2(encoding[1:]) + take_2(encoding[2:])
        else:
            return take_2(encoding[1:])

test = take_2("1234")

