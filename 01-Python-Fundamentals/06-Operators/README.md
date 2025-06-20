# ⚙️ Python Operators - Complete Guide

In Python, **operators** are special symbols used to perform operations on variables and values. This guide covers all major types of operators with examples.

---

## 🧮 1. Assignment Operators
Used to assign values to variables and perform shorthand operations.
```python
name = "Dave"
number = 42
number += 1  # Add and assign
number -= 1  # Subtract and assign
number *= 10 # Multiply and assign
number /= 10 # Divide and assign
number = round(number)
number %= 10 # Modulo and assign
```

---

## ➕ 2. Arithmetic Operators
Used to perform basic mathematical operations.
```python
print(2 + 2)      # Addition
print(4 - 2)      # Subtraction
print(2 * 2)      # Multiplication
print(24 / 5)     # Division (float)
print(24 // 5)    # Floor Division (int)
print(24 % 5)     # Modulo (remainder)
print(2 ** 3)     # Exponentiation
```

---

## 🔗 3. String Concatenation
```python
str1 = "Dave " + "Gray"
print(str1)  # Dave Gray
```

---

## 🧾 4. Comparison Operators
Used to compare values and return boolean results.
```python
print(42 == 41)  # Equal to → False
print(42 != 42)  # Not equal to → False
print(10 > 5)    # Greater than → True
print(10 < 5)    # Less than → False
print(10 >= 5)   # Greater than or equal → True
print(10 <= 5)   # Less than or equal → False
```

---

## 🧠 5. Logical Operators
Used to combine conditional statements.
```python
x = True
y = False
z = True

print(not x)     # False
print(x and y)   # False
print(x and z)   # True
print(x or y)    # True
```

---

## 🔍 6. Membership Operators
Test if a value is present in a sequence (like string, list, etc).
```python
print("a" in "apple")     # True
print(5 not in [1,2,3])   # True
```

---

## 🆔 7. Identity Operators
Compare the memory locations of two objects.
```python
a = [1, 2]
b = [1, 2]
print(a is b)    # False (different memory)
print(a == b)    # True (same values)
```

---

## 🧮 8. Operator Precedence
The order in which operations are performed in complex expressions (PEMDAS rule):
- **P**: Parentheses
- **E**: Exponents
- **MD**: Multiplication / Division
- **AS**: Addition / Subtraction
