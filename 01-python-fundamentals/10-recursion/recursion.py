"""
Recursion is when a function calls itself to solve a smaller version of the same position.
Always has a base to stop the recursion

Basic Structure (Syntax):
def recursive_function(): # Base case
    if condition_to_stop:
        return something
    else:
        return recursive_function() # Recursive call

"""

# factorial(7) - 7*6*5*4*3*2*1
# factorial(n) = n * factorial(n-1)

# Calculating factorial using recursion function


def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


factorial(3)
factorial(4)
factorial(5)

# return value after every iterations of recursion function
# 5 * factorial(5 - 1)
# 5 * factorial(4)
# 5 * 4 * factorial(4 - 1)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(3 - 1)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(2 - 1)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1 = 120
