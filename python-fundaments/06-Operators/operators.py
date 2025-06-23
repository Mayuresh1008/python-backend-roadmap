""" 
Python Operators:
Symbols used to perform operations on values and the variables that hold those values.
"""

# Assigment Operator
name = "Dave"
print(name)
number = 42
print(number)
number += 1
print(number)
number -= 1
print(number)
number *= 10
print(number)
number /= 10
print(number)
number = round(number) # round up the decimal value into integer
print(number)
number %= 10
print(number)

# # Arithmetic Operator
print("")
print(2 + 2) # Addition
print(4 - 2) # Subtraction
print(2 * 2) # Multiplication
print(24 / 5) # Division
print(24 // 5) # Floor Division
print(round(24 / 5)) # Round up value to 5
print(24 % 5) # Modular Division return remainder
print(2 ** 3) # returns exponent
print(2 ** 5)

# Concatenation
print("")
str1 = "Dave "  + "Gray"
print(str1)

# Comparison Operator
print("")
print(42 == 41) # returns false both values are not equal
print(42 == 42) # returns true both values are equal
print(42 != 42) # returns false both values are equal
print(42 != 42) # returns true both values are not equal
print(10 > 5) # greater than operator
print(10 < 5) # less than operator
print(10 >= 5) # greater than equal to operator
print(10 <= 5) # less than equal to operator
print("")

# Logical Operators
x = True
y = False
z = True
print(not x) # inverts the value of x
print(not y) # inverts the value of y
print(x and y) # Returns False both values are not True
print(x and z) # Returns False both values are True
print(y and z)
print(x or y) # Returns True if one value is True else returns False
print(x or z)
print(y or z)
print(y or x)

# Membership Operators
print("")
print("a" in "apple") # Returns True 
print(5 not in [1,2,3]) # Returns True 

# Identity Operators
a = [1,2]
b = [1,2]
print("")
print(a is b) # False (different objects)
print(a == b) # True
print("")

# Operator Precedence
""" 
Understand the PEMDAS acronym:
> Parentheses
> Exponents
> Multiplication / Division (will be solved according to their occurrence means the operator which comes first will be solved first)
> Addition / Subtaction (will be solved according to their occurrence means the operator which comes first will be solved first)
"""
result = 5 + 3 * 2
print(result)  

result = (5 + 3) * 2
print(result)  

result = 10 ** 2 / (4 + 5) * 3
print(result)  



