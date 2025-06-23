""" 
There are 4 types of functions in Python:

1. No parameter, no return - Function with No Parameters and No Return:
>> Function doesn't take any input , doesn't give any result back and just performs a task like printing something.

2. With parameter, no return - Function with Parameters and No Return:
>> Function takes input (parameters), doesn't return anything and performs a task

3. No parameter, with return - Function with No Parameters but with Return
>> Function doesn't take any input, but gives back a value using return

4. With parameter and return - Function with Parameters and Return
>> Function takes inputs, returns the result and performs the calculation and logic.
"""

## 1. Functions with No Parameters and No Return

# Example 1:
def welcome():
    print("Welcome to the Python course!")

welcome() 

print("")

# Example 2:
def show_date():
    print("Today is Saturday.")

show_date() 

print("")

# Example 3:
def say_hello():
    for i in range(3):
        print("Hello!")

say_hello()

## 2. Function with Parameters and No Return 

print("\n\n\n")

# Example 1:
def greet(name):
    print(f"Hi, {name}! Have a great day!")

greet("Mayuresh")

print("")

# Example 2:
def print_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

print_table(7)

print('')

# Example 3:
def print_even_numbers(limit):
    for i in range(2, limit+1, 2):
        print(i, end=" ")

print_even_numbers(10)


print("\n\n\n")

## 3. Function with no parameters but with return

# Example 1:
def get_pi():
    return 3.14159

pi = get_pi()
print("Value of pi:", pi)

print("")

# Example 2:
def default_username():
    return "guest_user_001"

print("Auto-generated username:", default_username())

print("")

# Example 3:
def lucky_number():
    import random
    return random.randint(1, 100)

print("Your lucky number is:", lucky_number())

print("\n\n\n")

## Function with Parameters and Return

# Example 1:
def add(a, b):
    return a + b

sum_result = add(10, 5)
print("Sum:", sum_result)

print("")

# Example 2:
def is_even(num):
    return num % 2 == 0 # adding condition in return statement

print("Is 7 even? ", is_even(7))
print("Is 10 even? ", is_even(10))

# Example 3:
def find_area(length, width):
    return length * width

print("Area of rectangle:", find_area(5, 8))