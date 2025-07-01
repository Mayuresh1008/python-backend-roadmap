# 🔁 Python Recursion

Recursion is a powerful technique where a function **calls itself** to solve smaller sub-problems of a larger problem.

---

## 📘 What is Recursion?
A recursive function is a function that calls itself until a base condition is met.

### 🧠 Basic Syntax:
```python
def recursive_function():
    if condition_to_stop:        # Base case
        return something
    else:
        return recursive_function()  # Recursive call
```

---

## 📌 Factorial Example (Recursive)

```python
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(3))  # 6
print(factorial(4))  # 24
print(factorial(5))  # 120
```

### 🔍 Execution Flow for factorial(5):
```
5 * factorial(4)
5 * 4 * factorial(3)
5 * 4 * 3 * factorial(2)
5 * 4 * 3 * 2 * factorial(1)
5 * 4 * 3 * 2 * 1 = 120
```

---
