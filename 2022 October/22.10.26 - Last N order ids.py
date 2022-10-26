# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 16:35:50 2022

@author: abelw

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

"""

class id_log():
    def __init__(self, data=[], N=10):
        self.data = data
        self.N = N
    
    def record(self, order_id):
        self.data.insert(0,order_id)
        if len(self.data) > self.N:
            self.data.pop()

    
    def get_last(self,i):
        return self.data[i-1]

test = id_log([])

for x in range(0,20):
    test.record(x)

print(test.get_last(10))