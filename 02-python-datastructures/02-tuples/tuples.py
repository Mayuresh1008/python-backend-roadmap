"""
A tuple is like a list, but immutable (you cannot modify it after creation).
Think of it as a read-only list (It is used when you don't want data to change).
"""

# Creating Tuples
# normal
t1 = (1, 2, 3)
print(t1)

# parenthesis are optional
t2 = 1, 2, 3
print(t2)

# single-element tuple
single = (42,)
# not_tuple = (42)

print(single)
# print(not_tuple)

# empty tuple
empty = ()
print(empty)

# Accessing & Slicing
t = ("apple", "banana", "orange")
print(t[0])
print(t[1])
print(t[-1])

# Tuple Unpacking
record = ("Mayuresh", "active", 42)

name, status, count = record
print(name)
print(status)
print(count)

# Extended unpacking
nums = (1, 2, 3, 4, 5)
first, *middle, last = nums
print(first, middle, last)

# Immutability
t = (1, 2, 3)
# t[0] = 10 # TypeError

# But if there is a list within the tuple then
t = ([1, 2], 99)
print(t)
t[0].append(3)
print(t)

# Common Methods
t = (1, 2, 2, 3)
print(t.count(2))
print(t.index(3))
