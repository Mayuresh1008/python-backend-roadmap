""" 
For loop - When You Know How many Times to Repeat the same task
loop starts from 0 by default
"""
# Simple example

name = "Abhishek"
for i in name:
    # print(i)
    print(i, end = " ")

print("")

# Iterating through lists
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)

""" 
# Nested for loop
for color in colors:
    print(color)
    for i in color:
        print(i)
"""

# range function (range goes from start to n-1)
""" 
Syntax : range(start, stop, step)
"""

# range(stop) : when singe argument is added
print("")
for i in range(5):
    print(i)

# range(start, stop)
print("")
for i in range(3, 8): # starts from 3 and ends at (n-1) it means this will stop at 7
    print(i)

# range(start, stop, step) - Control the jump
print("")
for i in range(1, 12, 2): # jumps by 2 each time
    print(i)
    
# reverse loop : range(high, low, -1)
print("")
for i in range(5, 0, -1):
    print(i)

# Examples
