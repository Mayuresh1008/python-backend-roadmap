"""
Modules:
A module is just a Python file that contains functions, variables, or classes - which you can reuse in other Python Files.

It Helps in breaking code into smaller parts so your programs become clean and organized.

Types of Modules:
1) Built-in Modules - Already available in Python
2) Custom Modules - Created by user
3) External Modules - installed using pip
"""

## Built-in Modules
# math Module
import math

print(math.sqrt(16))
print(math.pow(2, 3))
print(math.floor(4.9))
print(math.ceil(4.1))
print(math.pi)

# random Module
import random

slist = [1, 2, 3, 6, 7, 8, 0]
print(random.randint(1, 10))
print(random.choice([1, 2, 3]))
random.shuffle(slist)
print("Shuffle list : ", slist)
