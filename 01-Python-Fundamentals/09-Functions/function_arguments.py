""" 
Functions Arguments and return statement 

There are four types of arguments that we can provide in a function:
> Default Arguments
> Keyword Arguments
> Required Arguments
> Variable length Arguments
"""

## Default Arguments - we can provide default value while creating a function

def average(a=9, b=1, c=2): # if we dont provide any value then this values are used by the function for execution
    print("The average is ", ((a + b + c)/ 3))
    
# average(4, 6)
average(1, 5, 6) # this values will replace the default values
average(5) # a=5,b will be the default value 1 
average(b=9) # here b=9, a will be the default value 9

## Another example
def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello, ", fname, mname, lname)

name("Amy")
name("Mayuresh", "Umesh", "Patil")

# ------------------------------------------------------------------------------------------------------------------------

## Keyword Arguments - we can provide arguments with key = value, this way the interpreter regonizes the arguments by the parameter name.

average(b=9, a=21) # Keyword arguments 

# Another example
def fullname(fname, mname, lname):
    print("Hello, ", fname, mname, lname)

fullname(mname = "Umesh", lname = "Patil", fname = "Mayuresh")

# ------------------------------------------------------------------------------------------------------------------------

## Required Arguments - we should must pass the arguments if their no default value of that parameter

average(5, 6, 1)

name("Peter", "Quill")

# ------------------------------------------------------------------------------------------------------------------------

## Variable Length Postional Arguments - *args
# Use *args when you want to accept multiple positional values, and don't know the exact number of input
# Python stores them as tuple

def averageOfNumbers(*numbers):
    # this function stores the parameters as tuples
    # print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ", sum/len(numbers))

averageOfNumbers(5, 6, 4)

# Another example 
def names(*name):
    print("Hello, ", *name)

print("James", "Buchanan", "Barnes") # printing a list of names


# ------------------------------------------------------------------------------------------------------------------------

