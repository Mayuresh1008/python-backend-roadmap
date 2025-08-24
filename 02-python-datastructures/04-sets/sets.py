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

# Membership Testing
# (Fast O(1))
nums = {10, 20, 30}
print(20 in nums)
print(50 in nums)

# FrozenSet (Immutable Set)
fs = frozenset([1, 2, 3])
# fs.add(4) # not allowed it will generate an error
# print(fs)

## Mini Project (Sets)
# Unique Email Collector
emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com", "c@gmail.com", "b@gmail.com"]

unique_emails = set(emails)
print("Unique Emails:", unique_emails)
print("Count:", len(unique_emails))
