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

## 🔐 Closures in Python

A **closure** is a function that remembers variables from its enclosing scope, even after the outer function has finished executing.

Closures occur when a nested function refers to a value defined in its outer function.

### ✅ Simple Closure Example:

```python
def f1():
    x = 88

    def f2():
        print(x)

    return f2

myResult = f1()
myResult()  # Output: 88
```

### ✅ Practical Closure Example:

```python
def code(num):
    def actual(x):
        return x**num
    return actual

f = code(2)
g = code(3)

print(f(3))  # 9
print(g(3))  # 27
```

### ✅ Outer Function Closure:

```python
def outer_function(msg):
    def inner_function():
        print("Message:", msg)
    return inner_function

say_hello = outer_function("Hello")
say_hello()  # Output: Message: Hello
```

### ✅ Real-World Closure Use:

```python
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

times3 = multiplier(3)
times5 = multiplier(5)

print(times3(10))  # 30
print(times5(10))  # 50
```

---

## ✅ Summary

| Concept     | Description                                                               |
| ----------- | ------------------------------------------------------------------------- |
| **Scope**   | Determines where a variable is accessible (LEGB rule)                     |
| **Closure** | Function remembers variables from outer scope even after outer has exited |

