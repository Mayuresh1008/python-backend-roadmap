# 📘 Python Strings - Complete Guide

This section covers everything you need to know about **Strings in Python** with examples, slicing techniques, and powerful string methods.

---

## 🔤 What is a String?
- A **string** is a sequence of characters enclosed in single `' '`, double `" "`, or triple `""" """` quotes.
```python
name = "Harry"
friend = 'Rohan'
anotherfriend = '''Lavish'''
apple = """He said, \"I want to eat an apple\""""
```

---

## 📌 Accessing Characters
Use indexing to access characters in a string:
```python
name = "Harry"
print(name[0])  # H
```

---

## 🔁 Looping Through Strings
```python
for character in name:
    print(character)
```

---

## ✂️ String Slicing
```python
fruit = "Mongo"
print(fruit[0:4])  # "Mongo"[0:4] = 'Mong'
print(fruit[-3:-1])  # from 3rd last to 2nd last char
print(fruit[::-1])  # Reverses the string
```

### 🔢 Slicing with Steps
```python
text = "Hello, World!"
print(text[::3])  # Every 3rd character: 'Hl r!'
```

---


## 🧱 Strings Are Immutable
You can't change a string in-place; instead, use methods that return modified versions.

---

## 🔧 String Methods
### Case Conversion:
```python
name = "Rocky"
print(name.upper())
print(name.lower())
```

### Whitespace Removal:
```python
greet = "   Hello!   "
print(greet.strip())
print(greet.lstrip())
print(greet.rstrip())
```

### Replace:
```python
sentence = "Hello there, Hello again"
print(sentence.replace("Hello", "Hi"))
```

### Split:
```python
names = "John,Alice,Peter"
print(names.split(","))
```

### Capitalize & Title Case:
```python
text = "introduction to python"
print(text.capitalize())  # First word capital
print(text.title())       # Each word capital
```

### Center Alignment:
```python
str1 = "Welcome"
print(str1.center(20, "-"))
```

### Count:
```python
str1 = "hello hello"
print(str1.count("hello"))  # 2
```

### Endswith:
```python
print(str1.endswith("hello"))
```

### Find & Index:
```python
print(str1.find("hello"))  # Returns index or -1
print(str1.index("hello"))  # Raises error if not found
```

---

## 🧪 Boolean Check Methods
```python
print("Hello123".isalnum())     # True
print("Hello".isalpha())        # True
print("123".isdigit())          # True
print("hello".islower())        # True
print("HELLO".isupper())        # True
print("Hello World".istitle())  # True
print("    ".isspace())         # True
print("Hello".isprintable())    # True
```

---


## 🔄 Case Swap
```python
text = "Python IS Fun"
print(text.swapcase())  # pYTHON is fUN
```

---


## 🔗 String Joining
```python
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)
```

---

## 🧩 String Formatting
### `.format()`
```python
name = "Alice"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
```

### f-Strings
```python
print(f"My name is {name} and I am {age} years old.")
```

### Decimal & Alignment
```python
pi = 3.14159
print(f"Pi: {pi:.2f}")
print(f"{'Left':<10}|{'Right':>10}")
```

---


## ✅ Summary
| Concept | Description |
|--------|-------------|
| Indexing | Accessing characters by position |
| Slicing | Extracting substring parts |
| Immutability | Strings can't be changed in-place |
| Methods | Built-in functions to manipulate strings |
| Formatting | Inserting variables into strings |

---
