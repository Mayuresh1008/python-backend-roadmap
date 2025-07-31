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

