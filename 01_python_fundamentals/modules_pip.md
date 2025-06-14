# 📦 Python Modules and pip – Beginner Guide

## 🔹 What are Python Modules?

Modules in Python are files that contain Python code — functions, variables, classes — which you can reuse in your projects.

### ✅ Types of Modules:

1. **Built-in Modules** – Already included in Python (e.g., `math`, `random`, `datetime`)
2. **User-defined Modules** – Python files (.py) you create yourself
3. **External Modules** – Created by other developers, you install them using `pip` (e.g., `requests`, `flask`, `pandas`)

### 🔍 How to Use a Module:

```python
import math

print(math.sqrt(16))  # Output: 4.0
```

---

## 🔹 What is pip?

`pip` is the Python package installer. It allows you to download and install external modules from PyPI (Python Package Index).

### ✅ Check if pip is installed:

```bash
pip --version
```

### 🔄 Upgrade pip:

```bash
python -m pip install --upgrade pip
```

---

## 🔹 Installing External Modules

To install a module:

```bash
pip install <module-name>
```

Example:

```bash
pip install requests
```

To install multiple modules:

```bash
pip install requests flask pandas
```

---

### 🔎 Check Installed Modules:

```bash
pip list
```

### 🗑️ Uninstall a Module:

```bash
pip uninstall <module-name>
```

---

## 🧠 Bonus: Creating Your Own Module

Create a file called `my_module.py`:

```python
def greet(name):
    return f"Hello, {name}!"
```

Now use it in another file:

```python
import my_module

print(my_module.greet("Mayuresh"))
```

---

## ⚠️ Common pip Issues and Fixes

| Error                                                 | Solution                                                               |
| ----------------------------------------------------- | ---------------------------------------------------------------------- |
| There was an error checking the latest version of pip | Check internet or ignore, or run `python -m pip install --upgrade pip` |
| pip not recognized                                    | Add Python to system PATH                                              |
| Permission denied                                     | Add `--user` or run with admin rights                                  |

---

Happy coding! 🚀
