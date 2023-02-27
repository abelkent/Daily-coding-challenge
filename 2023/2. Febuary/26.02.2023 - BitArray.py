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
        self.data = list()
        
        if (size <= 0) or (type(size) != int):
            raise ValueError("Proposed size must be positive integer")
        self.size = size

    
    def set(self, i, val):
        if i > self.size:
            raise IndexError("Proposed set index beyond scope of BitArray")
        if val not in [1,0]:
            raise ValueError("Proposed set value is not bit format")

        #Occurences for if val is 0
        if val == 0:
            if i in self.data:
                self.data.remove(i)
        
        #Occurences for if val is 1
        elif val == 1:
            if i not in self.data:
                self.data.append(i)
        
    def get(self, i):
        if i in self.data:
            print(1)
            return 1
        else:
            print(0)
            return 0

bitsy = BitArray(100)
bitsy.set(5,1)
bitsy.get(5)
bitsy.set(5,0)
print(bitsy.data)
#bitsy.set(101, 1)
