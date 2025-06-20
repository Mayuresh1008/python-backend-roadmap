""" 
String are immutable we can't change the string at the permanent but their are methods to change the string temporarily.

Strings Methods doesn't change the existing string they make a new string for the output which doesn't affects the original string
"""

name = "Rocky"
print(len(name)) # displays length of the string
print(name.upper()) # converts the string in uppercase.
print(name.lower()) # converts the string in lowercase.

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

sentence = "Hello, My name is John, doesn't you fell to say someone Hello"
print(sentence)
print(sentence.replace("Hello", "Hi")) # replaces all occurences of string hello with hi

names = "John,Alice,Peter"
print(names)
print(names.split(",")) # returns a list of substrings in the string, using sep as the separator string
# In this case "," is a separator(sep) which has created a list of names(substring) from the main string(names) separated by "," sep.

blogHeading = "introduction to python"
print(blogHeading)
print(blogHeading.capitalize()) # Converts the string into capatalized version
"""
The capatalize() method turns only the first letter of the string to uppercase and the rest other characters of the string are turned into lowercase
There is no effect if the first character is already uppercase.
"""

print(blogHeading)
print(blogHeading.title()) # Returns the string where every word is titlecased means every word's first letter will be in uppercase.


