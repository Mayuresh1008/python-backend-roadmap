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

## Examples of for loop:
# Example1 : Print number 1 to 5
print("")
for i in range(1, 6):
    print(i)

# Example2 : Print squares of numbers from 1 to 10
print("")
for i in range(1, 11):
    print(f"{i} * {i} = {i*i}")

# Example3 : Iterating through lists
print("")
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

# Example1 : Print table of 7
print("")
for i in range(1, 11):
    print(f"7 * {i} = {7 * i}")

# Example2 : Print even numbers from 2 to 20
print("")
for i in range(2, 21, 2):
    print(i)

# Example3 : Reverse loop for countdown
print("")
for sec in range(10, 0, -1):
    print(f"Countdown: {sec}")
print("Blast off!!!")