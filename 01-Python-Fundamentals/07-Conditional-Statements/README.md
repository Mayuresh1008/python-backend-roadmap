# 🧭 Python Conditional Statements 

Conditional statements let you control the flow of your program by executing code blocks based on conditions.

## ✅ If Statement
Executes code if the condition is true.
```python
age = 18
if age >= 18:
    print("You can vote!")
```

## 🔁 If-Else Statement
Provides an alternative when the `if` condition is false.
```python
age = int(input("Enter your age: "))
if age >= 18:
    print("You can drive")
else:
    print("You cannot drive")
```

## ➕ Elif Statement
Checks multiple conditions sequentially.
```python
num = int(input("Enter a number:"))
if num < 0:
    print("Number is negative")
elif num > 0:
    print("Number is positive")
elif num >= 999:
    print("Number is Special and out of range")
else:
    print("Number is zero")
```