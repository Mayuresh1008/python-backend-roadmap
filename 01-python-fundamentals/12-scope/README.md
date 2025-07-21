# 🧠 Python: Scopes and Closures

---

## 🔍 Scope in Python

**Scope** defines where a variable can be accessed in your code. Python follows the **LEGB Rule**:

* **L**ocal
* **E**nclosing
* **G**lobal
* **B**uilt-in

### ✅ Examples:

```python
# Global scope
username = "alex"

def func():
    # Local scope
    print(username)

print(username)
func()
```

```python
# Global, Enclosing, Local scope example
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()
print("Global:", x)
```

```python
# Using global keyword
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # Output: 1
```

---

