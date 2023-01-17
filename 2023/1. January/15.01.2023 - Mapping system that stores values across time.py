"""
Write a map implementation with a get function that lets you retrieve the value of a key at a particular time.

It should contain the following methods:

set(key, value, time): sets key to value for t = time.
get(key, time): gets the key at t = time.
The map should work like this. If we set a key at a particular time, it will maintain that value forever or until it gets set at a later time.

In other words, when we get a key at a time, it should return the value that was set for that key set at the most recent time.

Consider the following examples:

d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 2) # set key 1 to value 2 at time 2
d.get(1, 1) # get key 1 at time 1 should be 1
d.get(1, 3) # get key 1 at time 3 should be 2

d.set(1, 1, 5) # set key 1 to value 1 at time 5
d.get(1, 0) # get key 1 at time 0 should be null
d.get(1, 10) # get key 1 at time 10 should be 1

d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 0) # set key 1 to value 2 at time 0
d.get(1, 0) # get key 1 at time 0 should be 2
"""

#Creates class "temporal map"
class Temporal_Map():


    #Initialises object with an empty dictionary as "map"
    def __init__(self, map = dict()):
        self.map = map
    
    #Set function that assigns value/time pairs to key value in map dict
    def set(self, key, value, time):
        #Adds key to dict if not already present
        if key not in self.map.keys():
            self.map[key] = [[value,time]]

        #Updates associated value/time pairs if key already present
        else:
            cache = self.map.get(key)
            cache.append([value, time])
            self.map[key] = cache
        

    #Get function that returns value of key at given time value
    def get(self, key, time):

        #If key is not present in map returns None
        if key not in self.map.keys():
            print(None)
            return
        
        #Cache is set as stored values for given key
        cache = self.map.get(key)
        #Output is initialised as None
        output = None
        
        #For each pair in the map, if the time value is greater than or equal to provided time, updates output
        #NOTE: Assumes times are added in chronological order
        #NOTE: Could go in reverse order for reduced time complexity, stop when valid time identified
        for pair in cache:
            if time >= pair[1]:
                output = pair[0]
                print("Output set to "+str(output)+" at value/time pair: "+str(pair))
        
        #prints output
        print(output)
    
    #Custom user function to print dict to review changes
    def all_data(self):
        print(self.map)

d = Temporal_Map()
#d.set(1, 1, 0) # set key 1 to value 1 at time 0
#d.set(1, 2, 2) # set key 1 to value 2 at time 2
#d.get(1, 1) # get key 1 at time 1 should be 1
#d.get(1, 3) # get key 1 at time 3 should be 2

d.set(1, 1, 5) # set key 1 to value 1 at time 5
d.get(1, 0) # get key 1 at time 0 should be null
d.get(1, 10) # get key 1 at time 10 should be 1

d.all_data()