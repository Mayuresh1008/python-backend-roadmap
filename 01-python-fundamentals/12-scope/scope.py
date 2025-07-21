"""
Scope in Python:
Scope defines where a variable can be accessed in your code.
Python follows the LEGB Rule:
Local --> Enclosing --> Global --> Built-in

Closures in Python:
A closure is a function that remembers variables from its enclosing scope, even after the outer function has finished executing.
Closures happen when a nested (inner) function refers to a variable from the outer (enclosing) function, and that outer function has already completed.
"""

# scope in python
username = "alex"


def func():
    # username = "drake"
    print(username)


print(username)
func()

x = 99


# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)


# def func3():
#     global x
#     x = 12


# func3()
# print(x)

## Scope Example
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


# global Keyword
count = 0


def increment():
    global count
    count += 1


increment()
print(count)
