# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 18:35:49 2022

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

@author: abelw
"""



#Creating data stream
def populate_memory(scale):
    for index in range(scale):
        print(index)
        with open("22.10.25 - Supplementary file.txt","a") as file:
            file.write(str(index)+"\n")
    
    print("Complete")
    

def select_value(local_memory_scope):
    pass
        