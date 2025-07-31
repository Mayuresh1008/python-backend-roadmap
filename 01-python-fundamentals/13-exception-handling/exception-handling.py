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

# Example 4: List index finder
try:
    my_list = [10, 20, 30]
    idx = int(input("Enter index (0-2):"))
    print("Element:", my_list[idx])
except IndexError:
    print("That index is out of range.")
except Exception as e:
    print("Some other error occured:", e)

print("")
# Example 5: File Reader with finally
try:
    file = open("notes.txt", "r")
    content = file.read()
    print("File Content:\n", content)
except FileNotFoundError:
    print("File not found.")
finally:
    try:
        file.close()
    except:
        pass
    print("File closed.")

print("")


# Example 6: Student Marks Checker
class InvalidInputError(Exception):
    pass


def check_marks(num):
    if num < 0 or num > 100:
        raise InvalidInputError("The value is not in the range 0-100.")
    print("Valid mark!!")


try:
    marks = int(input("Enter the mark between (0-100): "))
    check_marks(marks)
    print("Your marks:", marks)
except InvalidInputError as e:
    print(e)
except ValueError:
    print("The input is not an integer.")
finally:
    print("Validation complete.")

print("")


# Example 7: ATM Withdrawal Simulator
class InsufficientFundsError(Exception):
    pass


class NegativeNumberError(Exception):
    pass


def check_amount(amount, balance):
    if amount < 0:
        raise NegativeNumberError("Amount can't be a negative number.")
    elif amount > balance:
        raise InsufficientFundsError("Insufficient Balance")
    else:
        new_balance = balance - amount
        print("Withdrawal Successful. Remaining balance:$", new_balance)
        return new_balance


balance = 5000

try:
    amount = int(input("Enter withdrawal amount:"))
    check_amount(amount, balance)
except ValueError:
    print("the input is not valid.")
except NegativeNumberError as e:
    print(e)
except InsufficientFundsError as e:
    print(e)
finally:
    print("Thank you for using the ATM.")
