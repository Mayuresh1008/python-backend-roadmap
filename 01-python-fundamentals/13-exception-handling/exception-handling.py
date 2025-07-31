"""
try : Block where you write code that may cause an error(exception).
Python "tries" to run this block

except : Block that catching and handles errors raised in the try block.
You can specify error types (like ZeroDivisionError, ValueError) or catch all.

else : Runs only if no error occurs in the try block. Often used to execute "safe" code.

finally : Runs no matter what - whether an error happened or not. Good for cleanup actions like closing files, ending connections.
"""

try:
    x = 1 / 0
except ZeroDivisionError:
    print("Can't divide by zero.")
else:
    print("Everything went fine.")
finally:
    print("This block always runs.")
