# 🧠 Python Exception Handling - Notes

Exception handling allows your program to deal with errors gracefully. Below are core concepts with different simple examples for each.

---

## ✅ `try`

Block that contains code which **might cause an error**.

```python
try:
    result = 10 / 0
```

---


## ❌ `except`

Block that **catches and handles the error** from the `try`.

```python
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

You can also use:

```python
except Exception as e:
    print("Error occurred:", e)
```

---

## 🟢 `else`

Runs **only if no error** occurs in the `try` block.

```python
try:
    num = int("42")
except ValueError:
    print("Invalid number.")
else:
    print("Conversion successful:", num)
```

---

## 🧹 `finally`

Runs **no matter what** — whether an exception occurred or not.

```python
try:
    f = open("file.txt", "r")
except FileNotFoundError:
    print("File not found.")
finally:
    print("This runs always.")
```

---

## ⚠️ `raise`

Used to **manually trigger an exception**.

```python
age = -5
if age < 0:
    raise ValueError("Age cannot be negative.")
```

---

## 🧱 `Exception`

Base class for all built-in exceptions. Use it to **catch any type of error**.

```python
try:
    x = int("abc")
except Exception as e:
    print("Caught:", e)
```

---

## ✨ Custom Exception

You can define your **own error types** by inheriting from `Exception`.

```python
class TooShortNameError(Exception):
    pass

name = "Al"
if len(name) < 3:
    raise TooShortNameError("Name is too short.")
```

---

## 🔥 Common Built-in Exceptions

| Exception Type      | Description                                |
| ------------------- | ------------------------------------------ |
| `ZeroDivisionError` | Division by zero (`5 / 0`)                 |
| `ValueError`        | Invalid type conversion (`int("abc")`)     |
| `TypeError`         | Invalid operation between mismatched types |
| `IndexError`        | Index out of range for list                |
| `KeyError`          | Accessing a missing dictionary key         |
| `FileNotFoundError` | File doesn’t exist                         |

---

> ✅ Tip: Use `finally` for cleanup and `raise` to enforce rules in your code.
