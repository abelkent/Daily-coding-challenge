""""
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
"""

def power_set_generator(original):

    powerset = list() #Generates empty list as powerset (using set generates unhashable error)


    format_id = "0"+str(len(original))+"b" #Generate appropriate binary format code

    #Populates set dict with each index keying to corresponding value in set
    set_dict = dict()
    for index, element in enumerate(original):
        set_dict[index] = element


    max_int = 2**len(original) #Gets the integer required for binary representation of all elements of powerset

    for permutation in range(max_int): #Iterates through binary value corresponding to subset
        local_set = set() #Generates blank local_set
        permutation = (format(permutation, format_id)) #Permutation converted to binary format of appropriate length
        for index in range(len(permutation)): #For character in permutation ...
            if permutation[index] == "1": #... if character is a "1" ...
                local_set.add(set_dict[index]) #...corresponding value is added to local_set
        
        #local_set added to powerset
        powerset.append(local_set)
        #local_set reset
        local_set = {}
    
    #Prints powerset
    print(powerset)
            

power_set_generator({2, 4, 6})