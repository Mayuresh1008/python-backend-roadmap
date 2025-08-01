## TASK 1
# Remove Duplicates Without Using Set
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []

for x in my_list:
    if x not in unique_list:
        unique_list.append(x)

print("Original List:", my_list)
print("List without duplicates:", unique_list)

print("")
## TASK 2
# Find ALL Pairs That Add Up to a Target
numbers = [2, 4, 3, 5, 7, 8]
target = 10

pairs = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            pairs.append((numbers[i], numbers[j]))

print("Pairs that sum to", target, ":", pairs)

print("")
## TASK 3
# Flatten a 2D list
a_2d_list = [[1, 2], [3, 4], [5]]
flatten_list1 = []
flatten_list2 = []

for pair in a_2d_list:
    flatten_list1.extend(pair)

print(flatten_list1)

# or

for pair in a_2d_list:
    for x in pair:
        flatten_list2.append(x)

print(flatten_list2)

# or

flattend = [x for sublist in a_2d_list for x in sublist]
print(flattend)


print("")

## TASK 4: Split list into Chunks
the_list = [1, 2, 3, 4, 5, 6, 7, 8]
chunk_size = 3

chucked_list = []

current_chunk = []

for item in the_list:
    current_chunk.append(item)

    if len(current_chunk) == chunk_size:
        chucked_list.append(current_chunk)
        current_chunk = []

# Add remaining items if any
if current_chunk:
    chucked_list.append(current_chunk)

print(chucked_list)

print("")
## TASK 5: Frequency Counter
numbers = [1, 2, 2, 3, 3, 3]
frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)
