## Lists are ordered, mutable, and can store elements of different data type.

# Creating Lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.5, True]

print(fruits)
print(numbers)
print(mixed)

# Indexing & Slicing
print(fruits[0])
print(fruits[-1])
print(fruits[1:])

# Modifying Lists (Mutable)
fruits[1] = "mango"  # Replaces "banana" with "mango"
print(fruits)

# Common lists Methods
fruits.append("orange")
print(fruits)

fruits.insert(1, "grapes")
print(fruits)

fruits.remove("cherry")
print(fruits)

last = fruits.pop()
print(last)
print(fruits)

count = fruits.count("apple")
print(count)

length = len(fruits)
print(length)

# fruits.sort()
fruits.sort(reverse=True)
print(fruits)

fruits.reverse()
print(fruits)

# Looping through lists
for fruit in fruits:
    print(fruit)

# List Comprehension (Mini Loop)
squares = [x * x for x in range(1, 6)]
print(squares)
