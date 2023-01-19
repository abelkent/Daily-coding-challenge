"""
Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.

A solution will always exist.

Example:

Input: 4
Output: 2 + 2 = 4
If there are more than one solution possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then

[a, b] < [c, d]
If a < c OR a==c AND b < d.

NOTE: UNSURE OF LEXICOGRAPHICAL SIZE
"""

#Supplementary prime checker function (slow, functions in n time)
def simple_prime_checker(number):
    #For divisor from 3 up to given number...
    for divisor in range(2,number-1):
        #...checks if number divides perfectly by divisor, if so, returns False as is not a prime number
        if (number % divisor == 0):
            return False
    #Returns true if no divisors are found (ergo, is a prime number)
    return True


#Function definition
def goldbach_sum_finder(number):

    #Checks if input is an even number
    if (number % 2) != 0:
        print("This number is not even")
        return

    #Prime value initialisation
    prime_a, prime_b = None,None

    #Counts backwards from number-1 to 0, checking if each number is prime
    for potential_a in range(number-1, 0,-1):
        if simple_prime_checker(potential_a) == True:

            #After finding the largest prime, sets prime_a to this value
            prime_a = potential_a
            
            #Counts backwards from largest prime to zero, checking each number is prime
            for potential_b in range(prime_a,0,-1):
                
                if simple_prime_checker(potential_b) == True:
                        
                    #When a prime number is found that sums with the first to make the input, returns the pair
                    if (potential_b + prime_a) == number:
                        prime_b = potential_b
                        print(prime_a, prime_b)
                        return (prime_a, prime_b)

goldbach_sum_finder(10234)