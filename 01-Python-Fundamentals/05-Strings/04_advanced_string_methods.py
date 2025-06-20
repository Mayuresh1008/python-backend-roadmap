# This are Advanced String Methods

## String Joining
# .join() method
""" 
Combines a list of strings into a single string using a separator.
Faster than "+" for large strings
"""
words = ["Python", "is", "awesome"]
sentence = " ".join(words) # Joins with space separator
print(sentence)

## String Formatting
# .format() (older method)
name = "Alice"
age = 25
print("My name is {} and I'm {} years old.".format(name, age))

# f-strings (new method)
print(f"My name is {name} and I'm {age} years old.")

## Advanced Formatting