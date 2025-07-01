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

## 📌 Fibonacci Series using Recursion

### 🔸 Logic:
- f(0) = 0
- f(1) = 1
- f(n) = f(n-1) + f(n-2)

```python
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

### 🧪 Usage:
```python
num = int(input("Enter the number of character in series: "))
print("calculation :", fibonacci(num))
```

---

## 📌 Print Fibonacci Series using Recursion

```python
def print_fibonacci_series(index, n):
    if index < n:
        print(fibonacci(index), end=" ")
        print_fibonacci_series(index + 1, n)

terms = int(input("Enter the number of terms: "))
print("Fibonacci series : ")
print_fibonacci_series(0, terms)
```

---

## 📌 Countdown using Recursion

```python
def countdown(n):
    if n == 0:
        print("Blast off!!!")
    else:
        print(n)
        countdown(n - 1)

countdown(10)
```

---
