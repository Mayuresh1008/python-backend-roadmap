""" 
Functions Arguments and return statement 

There are four types of arguments that we can provide in a function:
> Positional Arguments
> Default Arguments
> Keyword Arguments
> Required Arguments
> Variable Length Positional Arguments
> Variable Length Keywords Arguments
"""

## Positional Arguments - Values passed to a function in the same order as parameters are defined.
def average(a, b, c):
    print("The average is ", ((a + b + c)/ 3))

average(5, 6, 7)

# Another example 
def name(fname, mname, lname):
    print("Hello, ", fname, mname, lname)

name("Mayuresh", "Umesh", "Patil")

# One more example
def student(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

student("Mayuresh", 22, "Vadodara")

# ------------------------------------------------------------------------------------------------------------------------
print("")
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

# One More Example
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet() # Uses default
greet("Mayuresh") # Overrides default

# ------------------------------------------------------------------------------------------------------------------------
print("")
## Keyword Arguments - we can provide arguments with key = value, this way the interpreter regonizes the arguments by the parameter name.

# calling average function from above
average(b=9, a=21) # Keyword arguments 

# Another example
def fullname(fname, mname, lname):
    print("Hello, ", fname, mname, lname)

fullname(mname = "Umesh", lname = "Patil", fname = "Mayuresh")

# One more example 
def student(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

student(age=21, city="Vadodara", name="Mayuresh")
# ------------------------------------------------------------------------------------------------------------------------
print("")
## Required Arguments - we should must pass the arguments if their no default value of that parameter

average(5, 6, 1)

name("Peter", "Quill")

# ------------------------------------------------------------------------------------------------------------------------
print("")
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

print("James", "Buchanan", "Barnes") # printing a tuple of names

# One more example
def add_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    print("Sum is : ", total)
    
add_numbers(10, 20)
add_numbers(1, 2, 3, 4, 5)

# ------------------------------------------------------------------------------------------------------------------------

print("")
## Variable Length Keyword Arguments - **kwargs
# Use **kwargs when you want to accept multiple keyword arguments.
# Python stores them as a dictionary

def full_name(**name):
    # print(type(name))
    print("Hello", name["fname"], name["mname"], name["lname"])
 

full_name(mname = "Buchanan", lname = "Barnes", fname = "James")

# One more example 
def show_profile(**details):
        for key, value in details.items():
            print(f"{key} : {value}")
            
show_profile(name="Mayuresh", age=21, city="Vadodara", profession="Developer")

# ------------------------------------------------------------------------------------------------------------------------
print("")
## Return Statement - It is used to return the value of the expression back to the calling function.

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)

avg = average(5, 3, 6, 2)
print("Average of numbers: ", avg)

# Another example
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("Mayuresh", "Umesh", "Patil"))

# example of returning single value
def square(n):
    return n * n

print(square(4))

# example of returning multiple values
def calc(a, b):
    return a + b, a - b, a * b

add, sub, mul = calc(10, 5)

# Return nothing (None)
def show():
    print("Hello")

result = show()
print(result)

# ----------------------------------------------------------------------------------------------------------------------


# Example of All Argument Types:
def student_info(name, age=18, *hobbies, **details):
    print(name, age, hobbies, details)

student_info("Mayuresh", 20, "cricket", "Music", city="Vadodara", grade="A")
