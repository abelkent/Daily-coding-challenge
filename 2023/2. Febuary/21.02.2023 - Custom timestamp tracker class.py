"""
Design and implement a HitCounter class that keeps track of requests (or hits). It should support the following operations:

record(timestamp): records a hit that happened at timestamp
total(): returns the total number of hits recorded
range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)
Follow-up: What if our system has limited memory?
"""

class HitCounter():
    def __init__(self):
        self.timestamps = list()
    
    def record(self, timestamp):
        self.timestamps.append(timestamp)
    
    def total(self):
        print (len(self.timestamps))
        return (len(self.timestamps))
    
    def range(self, lower, upper):
        hits_in_range = int(0)
        for timestamp in self.timestamps:
            if timestamp in range(lower, upper+1):
                hits_in_range+= 1

        print (hits_in_range)
        return hits_in_range

counter = HitCounter()
counter.record(1)
counter.record(3)
counter.record(5)
counter.total()
counter.range(1,3)