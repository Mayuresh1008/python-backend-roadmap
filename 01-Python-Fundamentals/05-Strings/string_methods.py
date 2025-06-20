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


