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

print("\n\n")
## TASK 1
numbers = [5, 3, 8, 6, 7, 2]
print(numbers)

# sorting the list in ascending and descending order
# ascending order
numbers.sort()
print(numbers)
# descending order
numbers.sort(reverse=True)
print(numbers)

# appending 10
numbers.append(10)
print(numbers)
# removing 3
numbers.remove(3)
print(numbers)

# printing squares of each number using list comprehension
squares = [x * x for x in numbers]
print(squares)

print("\n\n")
## TASK 2
friends = ["John", "Alice", "Angela", "Dave", "Max"]
print(friends)

# replacing a name
friends[2] = "Husn"
print(friends)

# add name at the start and at the end
friends.append("Angela")
print(friends)

friends.insert(0, "Lucky")
print(friends)

# printing all names using a loop
for name in friends:
    print(name)

## TASK 3

# printing length of a list
print(len(friends))

# counting the repeated item
# adding new items in a list to clarify more
numbers.append(2)
numbers.insert(1, 2)
print(numbers)
count = numbers.count(2)
print(f"there are {count} (2's) in the list.")

# printing index of a particular name
print(friends.index("Husn"))
