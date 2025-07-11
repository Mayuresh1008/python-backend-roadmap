# 📦 Python Modules

A **module** is simply a Python file containing **functions, variables, or classes**, which you can reuse in other Python files to keep your code organized and clean.

It helps break your code into smaller, reusable parts to improve readability, maintainability, and reduce redundancy.

---

## 🛠️ Types of Modules in Python

| Type               | Description                                        | Example                   |
|--------------------|----------------------------------------------------|---------------------------|
| **Built-in Modules** | Already available in Python's Standard Library    | `math`, `random`, `time`  |
| **Custom Modules**   | Created by the user to reuse personal code       | `calculator.py`, `mymodule.py` |
| **External Modules** | Installed via `pip`, developed by third parties | `numpy`, `requests`, `pandas` |

---

## ✅ Built-in Modules

### 🔹 Example: `math` Module
```python
import math

print(math.sqrt(16))
print(math.pow(2, 3))
print(math.floor(4.9))
print(math.ceil(4.1))
print(math.pi)
```

### 🔹 Example: `random` Module
```python
import random

slist = [1, 2, 3, 6, 7, 8, 0]
print(random.randint(1, 10))
print(random.choice([1, 2, 3]))
random.shuffle(slist)
print("Shuffled list:", slist)
```

### 🔹 Example: `time` Module
```python
import time

print(time.time())
time.sleep(2)
print(time.ctime())
```

> Some more modules : os, sys and so on

---

## 🧑‍💻 Custom Modules

You can create your own module by saving Python code in a `.py` file. Example: `calculator.py`

### Example content of `calculator.py`:
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
```
