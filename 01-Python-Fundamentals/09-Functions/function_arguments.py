""" 
Functions Arguments and return statement 

There are four types of arguments that we can provide in a function:
> Default Arguments
> Keyword Arguments
> Variable length Arguments
> Required Arguments
"""

def average(a=9, b=1): # if we dont provide any value then this values are used by the function for execution
    print("The average is ", (a + b/ 2))
    
# average(4, 6)
average(1, 5) # this values will replace the default values