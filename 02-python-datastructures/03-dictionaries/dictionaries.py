"""
A dictionary is a collection of key-value pairs.
Keys must be unique and immutable.
"""

## Creating Dictionaries

# Empty Dict
d1 = {}
print(d1)

# With values
d2 = {"name": "Mayuresh", "age": 22, "role": "Dev"}
print(d2)

# Using dict()
d3 = dict(name="Raj", age=21)
print(d3)

# Nested dict
d4 = {
    "student1": {"name": "Raj", "age": 20},
    "student2": {"name": "Mayuresh", "age": 22},
}

print(d4)

## Accessing & Updating
d = {"name": "Mayuresh", "age": 22}
print(d["name"])
print(d.get("role"))

d["role"] = "Dev"
d["age"] = 23

print(d)
