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
