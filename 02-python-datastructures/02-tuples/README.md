# 🐍 Tuples in Python

A **tuple** is like a list, but **immutable** (cannot be modified after creation).
Think of it as a **read-only list**, useful when you don’t want data to change.

---

## 📌 Creating Tuples

```python
# Normal tuple
t1 = (1, 2, 3)

# Parentheses are optional
t2 = 1, 2, 3

# Single-element tuple (must include a comma)
single = (42,)

# Empty tuple
empty = ()
```

✅ Output:

```
(1, 2, 3)
(1, 2, 3)
(42,)
()
```

---

## 📌 Accessing & Slicing

```python
t = ("apple", "banana", "orange")

print(t[0])   # apple
print(t[1])   # banana
print(t[-1])  # orange
```

---

## 📌 Tuple Unpacking

```python
record = ("Mayuresh", "active", 42)

name, status, count = record
print(name)    # Mayuresh
print(status)  # active
print(count)   # 42
```

---

## 📌 Extended Unpacking

```python
nums = (1, 2, 3, 4, 5)
first, *middle, last = nums

print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5
```

---

## 📌 Immutability

```python
t = (1, 2, 3)
# t[0] = 10  ❌ TypeError (cannot modify tuple)

# But if tuple contains a mutable object like a list:
t = ([1, 2], 99)
t[0].append(3)
print(t)   # ([1, 2, 3], 99)
```

---

## 📌 Common Methods

```python
t = (1, 2, 2, 3)

print(t.count(2))  # 2  → counts occurrences
print(t.index(3))  # 3  → returns first index of element
```

---

## 📌 Tuples as Dictionary Keys

Since tuples are immutable, they can be used as **dictionary keys** or **set elements**.

```python
coords = {}
coords[(10, 20)] = "Home"
coords[(30, 40)] = "Office"

print(coords)
# {(10, 20): 'Home', (30, 40): 'Office'}
```

---

## ✅ Summary

* Tuples are **immutable** lists.
* Use **commas** to create tuples (parentheses are optional).
* Great for **fixed collections** of data.
* Can be used as **dictionary keys** & **set elements**.
* Support **unpacking** & **slicing**.

🚀 Tuples are efficient, safe, and useful when you need data that should not be changed.
