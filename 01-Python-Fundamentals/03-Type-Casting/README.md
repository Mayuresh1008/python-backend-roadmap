# 🔁 Type Conversion (Type Casting) in Python

In Python, **type conversion** (also called type casting) is the process of converting one data type into another.

---

## 🔹 Two Types of Type Conversion

### 1️⃣ Implicit Type Conversion (Automatic)

Python **automatically converts** one type to another when possible.

```python
a = 5       # int
b = 2.5     # float

result = a + b

print(result)        # 7.5
print(type(result))  # <class 'float'>
```

In this case, Python automatically converted `int` to `float` to avoid data loss.

---

### 2️⃣ Explicit Type Conversion (Manual)

We manually convert one data type to another using built-in functions:

| Function  | Converts To                        |
| --------- | ---------------------------------- |
| `int()`   | Integer                            |
| `float()` | Float                              |
| `str()`   | String                             |
| `bool()`  | Boolean                            |
| `list()`  | List                               |
| `tuple()` | Tuple                              |
| `dict()`  | Dictionary (from key-value tuples) |

---

## 📘 Examples of Explicit Conversion

### 🔹 String to Integer / Float

```python
num_str = "100"
num_int = int(num_str)
num_float = float(num_str)

print(num_int)    # 100
print(num_float)  # 100.0
```

### 🔹 Integer to String

```python
age = 22
age_str = str(age)

print("I am " + age_str + " years old")  # I am 22 years old
```

### 🔹 Float to Integer

```python
price = 99.99
price_int = int(price)

print(price_int)  # 99 (decimal part removed)
```

### 🔹 List to Tuple

```python
my_list = [1, 2, 3]
my_tuple = tuple(my_list)

print(my_tuple)  # (1, 2, 3)
```

### 🔹 Tuple of Pairs to Dictionary

```python
items = [("a", 1), ("b", 2)]
items_dict = dict(items)

print(items_dict)  # {'a': 1, 'b': 2}
```

---

## ⚠️ Be Careful!

Not all conversions work:

```python
int("abc")  # ❌ Error: invalid literal for int()
```

Always ensure the value is compatible with the type you're converting to.

---

## 🧠 Summary

| Term                | Meaning                               |
| ------------------- | ------------------------------------- |
| Implicit Conversion | Python auto-converts safely           |
| Explicit Conversion | You use functions to convert manually |

Use `type()` to check data types before/after conversion.

---
