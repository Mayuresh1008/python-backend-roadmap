# 🧮 Variables & Data Types in Python

In Python, **variables** are used to store data. Python automatically decides the data type based on the value you assign.

---

## 📝 Declaring Variables

```python
name = "Mayuresh"
age = 22
is_student = True
height = 5.8
```

* No need to declare the type explicitly.
* Variable names should be meaningful and follow `lowercase_with_underscores` style.

---

## 🧠 What is a Data Type?

A **data type** tells Python what kind of data a variable holds — like numbers, text, lists, etc.

You can check a variable’s data type using the `type()` function:

```python
print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>
print(type(height))  # <class 'float'>
```

---

## 🔢 Common Python Data Types You’ve Learned

| Data Type | Example                                    | Description                                    |
| --------- | ------------------------------------------ | ---------------------------------------------- |
| `int`     | `age = 25`                                 | Whole numbers (positive or negative)           |
| `float`   | `height = 5.8`                             | Decimal numbers                                |
| `str`     | `name = "Mayuresh"`                        | Text or characters                             |
| `bool`    | `is_student = True`                        | Boolean values: `True` or `False`              |
| `complex` | `z = 2 + 3j`                               | Complex numbers with real and imaginary parts  |
| `list`    | `marks = [80, 85, 90]`                     | Ordered, changeable collection with duplicates |
| `tuple`   | `points = (1, 2)`                          | Ordered, unchangeable collection               |
| `dict`    | `person = {"name": "Mayuresh", "age": 22}` | Key-value pairs                                |

---

## 📘 Examples

### 🔹 Integer & Float

```python
x = 10      # int
y = 10.5    # float
```

### 🔹 String

```python
greeting = "Hello"
```

### 🔹 Boolean

```python
is_active = True
```

### 🔹 Complex

```python
z = 3 + 4j
```

### 🔹 List

```python
fruits = ["apple", "banana", "cherry"]
```

### 🔹 Tuple

```python
dimensions = (1920, 1080)
```

### 🔹 Dictionary

```python
user = {
    "name": "Mayuresh",
    "email": "mayuresh@example.com"
}
```

---

## 🔍 Using `type()` to Check Data Types

```python
a = 100
b = 5.6
c = "hello"
d = True

print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
print(type(d))  # <class 'bool'>
```

---

## 🧠 Quick Summary

* Variables hold values.
* Python auto-assigns the data type based on the value.
* You can check the data type using `type()`.
* Python supports many built-in data types: `int`, `float`, `str`, `bool`, `complex`, `list`, `tuple`, `dict`.

