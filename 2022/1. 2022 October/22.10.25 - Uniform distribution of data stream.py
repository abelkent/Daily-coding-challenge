# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 18:35:49 2022

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

@author: abelw
"""
import random


#Creating data stream
def populate_memory(scale):
    for index in range(scale):
        print(index)
        with open("22.10.25 - Supplementary file.txt","a") as file:
            file.write(str(index)+"\n")
    
    print("Complete")
    

#INCOMPLETE
def select_value(retrieval_register_size):
    retrieved_characters = []
    storage = open("22.10.25 - Supplementary file.txt","r")
    eof = False
    while not eof:
        batch = storage.readlines(retrieval_register_size)
        batch = [item.strip("\n") for item in batch]
        random_index = random.randint(0,retrieval_register_size)
        print(random_index)
        print(batch)
        eof = True
    

test = select_value(100)
    
        