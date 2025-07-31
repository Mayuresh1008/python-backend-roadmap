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

# Example 1 : Division with Multiple Exceptions

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
except ZeroDivisionError:
    print("ERROR: Cannot divide by zero")
except ValueError:
    print("ERROR: Please enter valid integers.")
else:
    print("Division result:", result)
finally:
    print("Program finished!!")

print("")


# Example 2 : Age Validator using raise and built-in error
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print("Valid age:", age)


try:
    user_age = int(input("Enter your age:"))
    check_age(user_age)
except ValueError as e:
    print("Caught error", e)


print("")


# Example 3 : Custom Exception for Negative Number
class NegativeNumberError(Exception):
    pass


def get_positive_numbers():
    num = int(input("Enter a positive number:"))
    if num < 0:
        raise NegativeNumberError("You entered a negative number.")
    return num


try:
    number = get_positive_numbers()
    print("Your number is:", number)
except NegativeNumberError as e:
    print("Caught Error:", e)
except ValueError:
    print("Enter valid integers.")

print("")
