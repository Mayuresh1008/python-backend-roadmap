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

## 🧠 Nested If Statements
Using if statements within other if statements.
```python
num = 18
if num > 0:
    if num <= 10:
        print("Number is between 1-10")
    elif num <= 20:
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
```

## 🪜 One-Line Conditionals (Ternary Operator)
Compact way of writing simple if-else.
```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
```

## 🔄 Boolean Logic in Conditions
Combining conditions with logical operators.
```python
if age >= 18 and has_id:
    print("Access granted")

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")

if not is_raining:
    print("No umbrella needed")
else:
    print("Take umbrella with you")
```

## ✔️ Truthy & Falsy Values
Python treats some values as `True` or `False` in conditions.
```python
name = "John"
if name:
    print("Hello, " + name)
else:
    print("No name provided")
```

> ✅ Use `if`, `elif`, and `else` to write smarter and cleaner decision-making code!


---

## 🧩 Match-Case Statements (Structural Pattern Matching)

Introduced in Python 3.10, `match-case` provides a powerful and clean way to handle multiple conditions — similar to switch-case in other languages but more flexible.

### 🔹 Basic Syntax
```python
match variable:
    case pattern1:
        # action1
    case pattern2:
        # action2
    case _:
        # default action
```

### 🔸 Basic Example
```python
status = 404
match status:
    case 200:
        print("Success")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown status")
```

### 🔸 Match with Conditions
```python
x = 40
match x:
    case 0:
        print("x is zero")
    case 1:
        print("x is one")
    case _ if x < 90:
        print(f"{x} is less than 90")
    case _:
        print(x)
```

### 🔸 Matching Literals
```python
day = "Monday"
match day:
    case "Monday" | "Tuesday":
        print("Weekday")
    case "Saturday" | "Sunday":
        print("Weekend")
```

### 🔸 Matching Tuples / Variables
```python
point = (1, 4)
match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"X-axis at {x}")
    case (0, y):
        print(f"Y-axis at {y}")
    case (x, y):
        print(f"Point at ({x}, {y})")
```