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

## Calculating factorial using recursion function


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


""" 
## Printing the fibonacci series using while loop
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, . . .
# f0 = 0
# f1 = 1
# f2 = f1 + f0
# fn = f(n - 1) + f(n - 2)


def while_fibonacci_series(n):
    num1 = 0
    num2 = 1
    fibo = []
    while n > 0:
        fibo.append(num1)
        num3 = num2 + num1
        num1 = num2
        num2 = num3
        n -= 1

    return fibo


num = int(input("Enter the number of character in series: "))
print("Fibonacci series: ", while_fibonacci_series(num))
print("calculation : ", fibonacci(num))
"""

## Calculating Fibonacci series


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


## Printing the fibonacci series using recursive functions
def print_fibonacci_series(index, n):
    if index < n:
        print(fibonacci(index), end=" ")
        print_fibonacci_series(index + 1, n)


terms = int(input("Enter the number of terms: "))

print("Fibonacci series : ")
print_fibonacci_series(0, terms)
# print("\nCalculation :", fibonacci(terms))
