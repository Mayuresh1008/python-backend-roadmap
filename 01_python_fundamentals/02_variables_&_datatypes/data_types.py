""" 
This is the practice file 
where i have practice about different datatypes, string methods,
removing whitespaces and displaying length of the string, justify
space of the string, string index values methods and modifications

"""



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



