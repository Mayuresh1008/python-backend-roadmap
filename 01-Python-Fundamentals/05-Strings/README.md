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
