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
