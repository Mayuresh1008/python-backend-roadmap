# 🧾 User Input in Python

Python allows you to get input from the user using the built-in `input()` function.

This is useful for making your programs interactive.

---

## 📥 Syntax

```python
input("Your message here: ")
```

The message inside the quotes is called a prompt — it tells the user what to type.

Whatever the user enters is returned as a string by default.

---

## 🧠 Example 1: Basic Input

```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

🟢 **Output (if user types "Mayuresh"):**

```
Enter your name: Mayuresh
Hello, Mayuresh!
```

---

## ⚠️ Important: All Input is a String by Default

Even if the user enters a number, it’s received as a string.

🔄 Convert it using `int()` or `float()`:

```python
age = input("Enter your age: ")
print(type(age))  # <class 'str'>

age = int(age)    # Convert to int
print(type(age))  # <class 'int'>
```

---

## 🧮 Example 2: Add Two Numbers from User

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
total = num1 + num2

print("Total:", total)
```

---

## 🔢 Example 3: Float Input

```python
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
total = price * quantity

print("Total price:", total)
```

---

## 🧠 Tips

* Always convert the input to the correct type (`int`, `float`, etc.) before using in calculations.
* You can combine input + conversion in one line:

```python
marks = int(input("Enter your marks: "))
```

---

## ✅ Summary

| Function           | Purpose                                   |
| ------------------ | ----------------------------------------- |
| `input()`          | Take input from user (always string)      |
| `int()`, `float()` | Convert string input to number            |
| `str()`            | Convert number back to string (for print) |

---
