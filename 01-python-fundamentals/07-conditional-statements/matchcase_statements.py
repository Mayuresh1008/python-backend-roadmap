""" 
Matchcase Statements:
match-case statements (also called as structured pattern matching) provides a powerful alternative to long if-elif-else chains.
It's similar to switch-case in other languages but more flexible.

Basic Syntax:
match value:
    case pattern1:
        # action1
    case pattern2:
        # action2
    case _: # default case
        # default action
"""
""" 
# Example
x = 40 # x is the variable to match

match x:
    # if x is 0
    case 0:
        print("x is zero")
    case 1:
        print("case is 1")
    case _ if x < 90:
        print(x, "is less than 90")
    case _ if x != 80:
        print(x, "is greater than 10")
    case _:
        print(x)
"""

# Simple Example
status = 404
match status:
    case 200:
        print("Success")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown status")

## Pattern Matching Features
# Matching Literals
day = "Monday"

match day:
    case "Monday" | "Tuesday":
        print("Weekday")
    case "Saturday" | "Sunday":
        print("Weekend")

# Matching with variables
point = (1, 4)
match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"X-axis at {x}")
    case (0, y):
        print(f"Y-axis at {y}")
    case (x, y):
        print(f"Point at ({x}, {y})")

# Matching with conditions (if in cases)
age = 17
match age:
    case x if x < 13:
        print("Child")
    case x if 13 <= x <= 20:
        print("Teen")
    case _:
        print("Adult")

        