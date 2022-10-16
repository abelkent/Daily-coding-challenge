# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 17:26:16 2022

@author: abelw
"""

class XOR_linked_list(list):
    def __init(self):
        super().__init__()
        
    def add(self, element):
        if len(self) == 0:
            both = None
            self.append([element, both])
            
        elif len(self) == 1:
            self[-1][1] = element
            both = self[-1][0]
            self.append([element, both])
            
        else:
            self[-1][1] = element ^ self[-2][0]
            both = self[-1][0]
            self.append([element, both])
        print(self)
            

        
    def get(self, index):
        return (self[index][0])

test = XOR_linked_list()
print(test)
a = 0
b = 5
c = a ^ b


test.add(1)
test.add(2)
test.add(3)
test.add(4)
test.add(5)
test2 = test.get(0)