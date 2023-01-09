"""
What does the below code snippet print out? How can we fix the anonymous functions to behave as we'd expect?

functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())
"""

"""
DISCUSSION
Code snippet prints out ten instances of "9", as opposed to the (presumably intended) output of 0 - 9.

Issue arises from how lambda calling of i makes every call of 9 call the final value of 9 rather than the leading values of 0-9.
"""

#NOT AS OF YET CORRECTED
