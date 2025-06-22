""" 
Functions Arguments and return statement 

There are four types of arguments that we can provide in a function:
> Default Arguments
> Keyword Arguments
> Variable length Arguments
> Required Arguments
"""

## Default Arguments
def average(a=9, b=1): # if we dont provide any value then this values are used by the function for execution
    print("The average is ", (a + b/ 2))
    
# average(4, 6)
average(1, 5) # this values will replace the default values
average(5) # a=5,b will be the default value 1 
average(b=9) # here b=9, a will be the default value 9

## Another example
def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello, ", fname, mname, lname)

name("Amy")
name("Mayuresh", "Umesh", "Patil")