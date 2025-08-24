"""
A set is an unordered collection of unique elements.
Think of it as a mathematical set (no duplicates)
"""

# Creating Sets
s1 = {1, 2, 3, 4}
print(s1)

s2 = set([3, 4, 5, 6])
print(s2)

empty = set()
print(empty)

# Adding & Removing Elements
s = {1, 2, 3, 5}
print(s)

s.add(4)
print(s)

s.remove(2)
print(s)

s.discard(5)
s.discard(6)
print(s)

print(s.pop())
print(s)

s.clear()
print(s)

# Set Operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)  # union
print(a & b)  # intersection
print(a - b)  # difference
print(a ^ b)  # symmetric difference
