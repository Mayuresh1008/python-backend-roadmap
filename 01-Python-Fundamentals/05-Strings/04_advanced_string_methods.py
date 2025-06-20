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
# Decimal places
pi = 3.1415926535
print(f"Pi rounded: {pi:.2f}") 
# Syntax: "variable_name" ":" "." "no._decimal_places" "f"

# Padding & Alignment
print(f"{'Left':<10}") # Left-aligned (10 spaces)
print(f"{'Right':>10}") # Right-aligned (10 spaces)
print(f"{'Center':^10}") # Center-aligned (10 spaces : 5 at each side)
