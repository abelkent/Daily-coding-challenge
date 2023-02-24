"""
You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:

init(arr, size): initialize with the original large array and size.
set(i, val): updates index at i with val.
get(i): gets the value at index i.
"""

example_array = list([0,0,0,0,0,3,0,1,0,5])
print(example_array)

class SparseArray():
    def __init__(self, arr, size):

        if size < len(arr):
            raise IndexError("Proposed maximum length of array less than provided array")

        self.size = size
        self.data = list()
        for index in range(len(arr)):
            entry = arr[index]
            if entry != 0:
                self.data.append([index,entry])
    
    def set(self, i, val):

        if i > self.size:
            raise IndexError("Proposed index out of range")

        for entry in self.data:
            if entry[0] == i:

                if val == 0:
                    self.data.remove(entry)
                else:
                   entry[1] = val
                return

        if val != 0:
            self.data.append([i,val])
    
    def get(self, i):
        if i > self.size:
            raise IndexError("Proposed Index is out of scope of defined SparseArray size")
        
        for entry in self.data:
            if entry[0] == i:
                print(entry[1])
                return (entry[1])

sparse = SparseArray(example_array, 100)
print(sparse.data)
sparse.set(12, 8)
print(sparse.data)
sparse.set(9,1)
print(sparse.data)
sparse.set(9,0)
print(sparse.data)
sparse.get(12)