""" 
This is the practice file 
where i have practice about different datatypes, string methods,
removing whitespaces and displaying length of the string, justify
space of the string, string index values methods and modifications,
Casting string to number, and casting number to string, 
Built - in functions, math functinos and so on.
"""


import math
# String Data Type

# literal assignment
first = "Dave"
last = "Gray"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# Constructor function to define string
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string 
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiline 
multiline = ''' 
Hey, how are you?

I was just checking in.      
                                All good?
'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods

print(first)
print(first.lower()) # converts string into lowercase
print(first.upper()) # converts string into uppercase
print(first)

print(multiline.title()) 
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                      "
multiline = "                             " + multiline
print(len(multiline))

print(len(multiline.strip())) # length after removing all the white spaces.
print(len(multiline.lstrip())) # length after removing the white spaces from left side.
print(len(multiline.rstrip())) # length after removing the white spaces from right side.

# Build a Menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")

# String index values
print(first[1]) # Displays element at 1 position
print(first[-1]) # Displays element at last position
print(first[1:-1]) # Displays string between 1 to last position
print(first[1:]) # Displays string from 1 position to till the end

# Some methods return boolean data
print(first.startswith("D")) # Checking that does the string starts with "D" letter.
print(first.endswith("Z")) # Checking that does the string ends with "Z" letter.

# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data types
# integer datatype
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float datatype
gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex datatype
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))

""" 
# Math functions
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))  

# Error if you attempt to cast incorrect data
# zip_value = int("New York")
"""