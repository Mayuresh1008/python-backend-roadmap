"""
A list is an ordered, mutable collection of elements.
Think of it like a dynamic array that can hold numbers, strings, or even other lists.
"""

# Creating lists
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []

print(numbers)
print(mixed)
print(empty)

# Indexing and Slicing
fruits = ["apple", "banana", "mango", "orange"]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(fruits[0])
print(fruits[-1])
print(fruits[1:3])
print(fruits[:2])
print(fruits[::2])
print(nums[::3])

# Adding and Removing Elements
fruits = ["apple", "banana"]

# Add
fruits.append("mango")
print(fruits)
fruits.insert(1, "grape")
print(fruits)
fruits.extend(["orange", "kiwi"])
print(fruits)

# Remove
fruits.remove("banana")
print(fruits)
print(fruits.pop())
print(fruits)
del fruits[0]
print(fruits)

# Searching in lists
numbers = [10, 20, 30, 40]
print(20 in numbers)
print(numbers.index(30))

# Iterating lists
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# List Comprehension
squares = [x * x for x in range(5)]
print(squares)
