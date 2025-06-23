name = "Harry"
friend = "Rohan"
anotherfriend = 'Lavish'
apple = """He said, 
Hi Harry
hey I am good
\"I want to eat an apple\""""

print("Hello, " + name)
# print(apple)

# Accessing characters of a string
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) # This throws an error

# Looping through the string
print("\nLets use a for loop")
for character in name:
    print(character)
    
# Few more examples
name = 'Alice' # String with single quotes
greeting = "Hello, World!" # String with double quotes
poem = """Roses are red,
Violets are blue""" # Multiline String

print(name + "\n" + greeting + "\n" + poem) # Printing three things once