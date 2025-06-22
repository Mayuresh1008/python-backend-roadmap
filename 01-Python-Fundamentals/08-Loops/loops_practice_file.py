"""
# break statement
value = 1
while value <= 10:
    print(value)
    if value == 5:
        break
    value += 1
"""

""" 
# continue statement
value = 0
while value <= 10:
    value += 1
    if value == 5:
        continue
    print(value)
else:
    print("Value is now equal to: " + str(value))
""" 

""" 
# iterating through list
print("")
names = ["Dave", "Sara", "John"]
for x in names:
    print(x)
"""

""" 
# interating through string
for x in "Mississippi":
    print(x)
"""

""" 
print("")
for x in names:
    if x == "Sara":
        break
    print(x)    
"""

""" 
print("")
for x in names:
    if x == "Sara":
        continue
    print(x)
"""  
  
""" 
## range function examples
print("")
for x in range(4):
    print(x)

print("")
for x in range(2, 4):
    print(x)

print("")
for x in range(0, 101, 5): # number increments by 5
    print(x)
else:
    print("Glad that\'s over")
"""

# Nested loops
names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

for name in names:
    for action in actions:
        print(name + " " + action + ".")

print("")
for action in actions:
    for name in names:
        print(name + " " + action + ".")
    

