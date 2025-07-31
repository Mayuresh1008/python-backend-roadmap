"""
try : Block where you write code that may cause an error(exception).
Python "tries" to run this block

except : Block that catching and handles errors raised in the try block.
You can specify error types (like ZeroDivisionError, ValueError) or catch all.
"""

try:
    x = 1 / 0
except ZeroDivisionError:
    print("Can't divide by zero.")
