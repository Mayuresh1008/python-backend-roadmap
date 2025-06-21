# 🔁 Python Loops

Loops allow us to execute a block of code multiple times. Python provides two main types of loops: `for` loops and `while` loops.

---

## 🔹 For Loop
Use `for` loops when you know ahead of time how many times you want to iterate.

### ✅ Basic Example
```python
name = "Abhishek"
for i in name:
    print(i, end=" ")
```

### 🔸 Print Numbers
```python
# Print 1 to 5
for i in range(1, 6):
    print(i)

# Print squares of numbers 1 to 10
for i in range(1, 11):
    print(f"{i} * {i} = {i*i}")
```

### 🔸 Iterating Through Lists
```python
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)
```
