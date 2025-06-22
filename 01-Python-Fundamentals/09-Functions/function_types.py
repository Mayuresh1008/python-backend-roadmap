""" 
There are 4 types of functions in Python:

1. No parameter, no return - Function with No Parameters and No Return:
>> Function doesn't take any input , doesn't give any result back and just performs a task like printing something.

2. With parameter, no return - Function with Parameters and No Return:
>> Function takes input (parameters), doesn't return anything and performs a task

3. No parameter, with return - Function with No Parameters but with Return
>> Function doesn't take any input, but gives back a value using return

4. With parameter and return - Function with Parameters and Return
>> Function takes inputs, returns the result and performs the calculation and logic.
"""

## 1. Functions with No Parameters and No Return

# Example 1:
def welcome():
    print("Welcome to the Python course!")

welcome() # just shows the message no input needed

# Example 2:
def show_date():
    print("Today is Saturday.")

show_date() # just shows message, can't reuse or store anything

# Example 3:
def say_hello():
    for i in range(3):
        print("Hello!")

say_hello()