"""
> try : Block where you write code that may cause an error(exception).
Python "tries" to run this block

try:
    x = 1 / 0

> except : Block that catching and handles errors raised in the try block.
You can specify error types (like ZeroDivisionError, ValueError) or catch all.

except ZeroDivisionError:
    print("Can't divide by zero.")

> else : Runs only if no error occurs in the try block. Often used to execute "safe" code.

else:
    print("Everything went fine.")

> finally : Runs no matter what - whether an error happened or not. Good for cleanup actions like closing files, ending connections.

finally:
    print("This block always runs.")

> raise : You can raise to manually trigger an error. Useful when you want to enforce rules in your code.

raise ValueError("incorrect value")

> Exception : Base class for all the exceptions in Python.

except Exception as e:
    print(e)

> Custom Exception : You can create your own exception type by subclassing Exception.

class NegativeNumberError(Exception):
    pass

> ZeroDivisionError, ValueError, etc. : Built-in error classes in Python that represent specific problems:
ZeroDivisionError --> Division by zero
ValueError --> Invalid type conversion (e.g., int("abc"))
TypeError --> Invalid operation between mismatched types
IndexError --> Index out of range for lists
KeyError --> Missing key in dictionary
"""
