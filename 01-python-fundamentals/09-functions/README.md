# 📘 Python Functions

Functions are reusable blocks of code designed to perform a specific task. They help make your code modular, cleaner, and more organized.

---

## ✅ What Are Functions?
A function is a reusable block of code that performs a task.

### 🔹 Types of Functions:
1. Built-in Functions (e.g., `print()`, `input()`, `len()`)
2. User-defined Functions (created using `def` keyword)

### 🔹 Function Syntax:
```python
def function_name(parameters):
    # code block
    return value
```

---

## 🔄 Using Functions

### 🔸 Example: Calculating Geometric Mean
```python
def calculateGmean(a, b):
    mean = (a * b) / (a + b)
    print(mean)

calculateGmean(9, 8)
```

### 🔸 Example: Checking Greater Number
```python
def isGreater(a, b):
    if a > b:
        print("First number is greater")
    else:
        print("Second number is greater or both are equal")

isGreater(9, 7)
```

---

## 🔣 Function Arguments and Return Types

### 🔹 Positional Arguments
```python
def average(a, b, c):
    print("The average is", (a + b + c)/3)

average(5, 6, 7)
```

## 🔣 Function Arguments and Return Types

### 🔹 Positional Arguments
```python
def average(a, b, c):
    print("The average is", (a + b + c)/3)

average(5, 6, 7)
```

### 🔹 Default Arguments
```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Mayuresh")
```
