""" 
String are immutable we can't change the string at the permanent but their are methods to change the string temporarily.

Strings Methods doesn't change the existing string they make a new string for the output which doesn't affects the original string
"""
## Uppercase And Lowercase Methods
name = "Rocky"
print(len(name)) # displays length of the string
print(name.upper()) # converts the string in uppercase.
print(name.lower()) # converts the string in lowercase.

## Strip Method
greet = "    !!Hello!!!     "
print(greet)
print(greet.strip()) # removes white spaces from both sides
print(greet.rstrip()) # removes white spaces frrm just right side
print(greet.lstrip()) # removes whites spaces from left side

a = "!!!HI!!!!"
print(a)
print(a.strip("!")) # also removes unwanted character or symbols from the string at both sides.
print(a.rstrip("!")) # also removes unwanted character or symbols from the string at right side.
print(a.lstrip("!")) # also removes unwanted character or symbols from the string left side.

## Replace Method
sentence = "Hello, My name is John, doesn't you fell to say someone Hello"
print(sentence)
print(sentence.replace("Hello", "Hi")) # replaces all occurences of string hello with hi

## Split Method
names = "John,Alice,Peter"
print(names)
print(names.split(",")) # returns a list of substrings in the string, using sep as the separator string
# In this case "," is a separator(sep) which has created a list of names(substring) from the main string(names) separated by "," sep.

## Capitalize Method
blogHeading = "introduction to python"
print(blogHeading)
print(blogHeading.capitalize()) # Converts the string into capatalized version
"""
The capatalize() method turns only the first letter of the string to uppercase and the rest other characters of the string are turned into lowercase
There is no effect if the first character is already uppercase.
"""

## Title Method
print(blogHeading)
print(blogHeading.title()) # Returns the string where every word is titlecased means every word's first letter will be in uppercase.


## Centered Method
str1 = "Welcome to the Console!!!"
print(str1)
print(len(str1))
print(str1.center(50))
print(len(str1.center(50)))
# We can also add padding characters to the vacant space
print(str1.center(50,"-"))

# Count Method
print(str1.count("o")) # returns the number of times the given value has occurred within the given string.
print(sentence.count("Hello")) # returns 2

# Endswith Method
print(str1.endswith("!!!")) # checks if the string ends with given value or not and returns a boolean value True or False.
print(str1.endswith("to", 4, 10)) # checks if the string in the given index slice endswiths the given string or characters

# Find Method
""" 
The find() method searches for the first occurrence of the given value and returns the index where it is present. 
If given value is absent from the string then return -1.
"""
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))

# Index Method
""" 
The index() method searches for the first occurence of the given value and returns the index where it is present. If given value is absent from the string then raises an exception(error).
"""
print(str1.index("Dan")) 

# isalnum() Method
""" 
The isalnum() method returns True only if the string only consists of A-Z, a-z, 0-9.
If other characters or punctuation is found, it returns False.
"""
str1 = "WelcomeToMyConsole"
print(str1.isalnum())

# isalpha Method
""" 
Returns True if all the characters in the string are alphabet else returns False
"""
print(str1.isalpha())

# islower Method
str1 = "hello world"
"""
Returns True if all the characters in the string are in lowercase else returns False 
"""
print(str1.islower())

