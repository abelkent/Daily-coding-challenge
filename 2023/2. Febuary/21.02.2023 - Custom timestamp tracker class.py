"""
Design and implement a HitCounter class that keeps track of requests (or hits). It should support the following operations:

record(timestamp): records a hit that happened at timestamp
total(): returns the total number of hits recorded
range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)

Follow-up: What if our system has limited memory?
"""

#Implementation 1: Unconcerned with memory consumption

class HitCounter():
    def __init__(self):
        #Only local attribute is a blank array of timestamps (at initialisation) 
        self.timestamps = list()

    #Record adds timestamp to timestamp array
    def record(self, timestamp):
        self.timestamps.append(timestamp)
    
    #Total returns length of timestamp array
    def total(self):
        print (len(self.timestamps))
        return (len(self.timestamps))
    
    #Range returns number of hits within given range
    def range(self, lower, upper):
        hits_in_range = int(0)
        for timestamp in self.timestamps:
            if timestamp in range(lower, upper+1):
                hits_in_range+= 1

        print (hits_in_range)
        return hits_in_range

#Tests
"""counter = HitCounter()
counter.record(1)
counter.record(3)
counter.record(5)
counter.total()
counter.range(1,3)"""

#Implentation 2: More memory concerned

#Memory is now bounded by x as number of unique timestamps rather than n of timestamps but still not functioning in fixed memory 
class HitCounterConstrained():
    def __init__(self):
        self.data = dict()
    
    def record(self, timestamp):
        if timestamp not in self.data.keys():
            self.data[timestamp] = int(1)
        else:
            cache = self.data.get(timestamp)
            cache += 1
            self.data[timestamp] = cache
    
    def total(self):
        print (sum(self.data.values()))
        return sum(self.data.values())

    def range(self, lower, upper):
        hits_in_range = int(0)
        for timestamp in self.data.keys():
            if timestamp in range(lower, upper+1):
                cache = self.data.get(timestamp)
                hits_in_range += cache

        print(hits_in_range)
        return hits_in_range
    
counter = HitCounterConstrained()
counter.record(1)
counter.record(2)
counter.record(1)
counter.total()