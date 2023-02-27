"""
Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

init(size): initialize the array with size
set(i, val): updates index at i with val where val is either 1 or 0.
get(i): gets the value at index i.
"""

#NOTE: This seems like a more specialised SparseArray (re: 23/02/23) and will use similar implementation
#NOTE: On second thought, will try using dict implementation as considered in SparseArray implementation

class BitArray():
    def __init__(self, size):
        self.data = dict()
        self.size = size
    
    def set(self, i, val):

        if i >= self.size:
            raise IndexError("Propsed index for set() beyond defined size of BitArray")
        
        if val == 0:
            self.data.pop(i, 0)
            return

        if i not in self.data.keys():
            self.data[i] = val
        else:
            self.data.update(i, val)
    
    def get(self, i):
        
        if i in self.data.keys():
            return 1
        else:
            return 0
    #This makes me realise that both my implementation for this is innefficient, needs only record positon of 1s, hence dict is redundant

