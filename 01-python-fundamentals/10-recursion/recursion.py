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


print(factorial(3))
print(factorial(4))
print(factorial(5))
