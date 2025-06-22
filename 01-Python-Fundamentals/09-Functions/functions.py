""" 
Functions in Python - A function is a block of code that does something specific, and you can reuse it anywhere in your program

Types of functions:
1. Built-in functions
2. User-defined functions

Syntax:
def function_name(parameter): # function definiton
    # code block
    return value
"""

# Suppose calculating a geometric mean of two number
a = 9
b = 8
"""
# General method or way of doing
gmean = (a * b)/(a + b)
print(gmean)
"""

# Instead using function we can do like this
def calculateGmean(a, b): # function definition
    mean = (a * b)/(a + b)
    print(mean)

calculateGmean(a, b) # function call

# Another example of finding greater number between two number
""" 
# General method or way of doing
if a > b:
    print("First number is greater")
else:
    print("Second number is greater or both are equal.")
"""

# Using function we can do like this
def isGreater(a, b):
    if (a > b):
        print("First number is greater")
    else:
        print("Second number is greater or both are equal.")

c = 9
d = 7
isGreater(c, d)

def isLesser(a, b):
    pass # it is pretend like function code block is not written yet the developer will write the code or function later on just don't produce an error in short (pass is a placeholder).


