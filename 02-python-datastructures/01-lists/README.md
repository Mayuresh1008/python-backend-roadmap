# 📝 Python Lists - Notes

Lists in Python are ordered, mutable collections that can store elements of different data types. This guide includes syntax, methods, and practical tasks.

---

## 📌 Creating Lists

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.5, True]

print(fruits)
print(numbers)
print(mixed)
```

---

## 🔍 Indexing & Slicing

```python
print(fruits[0])      # First element
print(fruits[-1])     # Last element
print(fruits[1:])     # From index 1 to end
```

---

## ✏️ Modifying Lists

```python
fruits[1] = "mango"    # Replaces "banana" with "mango"
print(fruits)
```

---

## 🛠️ Common List Methods

```python
fruits.append("orange")      # Add to end
fruits.insert(1, "grapes")   # Insert at index 1
fruits.remove("cherry")      # Remove by value
last = fruits.pop()          # Remove last item
count = fruits.count("apple")
length = len(fruits)

fruits.sort(reverse=True)    # Sort descending
fruits.reverse()             # Reverse order
```

---

## 🔁 Looping Through a List

```python
for fruit in fruits:
    print(fruit)
```

---

## ⚡ List Comprehension

```python
squares = [x * x for x in range(1, 6)]
print(squares)
```

---

