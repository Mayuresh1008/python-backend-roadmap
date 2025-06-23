name = input("Enter your name: ")
print("My name is", name)

x = input("Enter first number: ")
y = input("Enter second number: ")
print(x + y) # concatenation
print(int(x) + int(y)) # addition

name = input("Enter your name: ")
print("Hello, " + name + "!")

age = int(input("Enter your age: "))
print("Next year, you'll be", age + 1)

# Multiple Inputs
x, y = input("Enter two numbers: ").split()
x = int(x)
y = int(y)
print("Sum:", x + y)

# Calculating age of user
birth_year = input("Enter your birth year:")
age = 2025 - int(birth_year)
print("Means, Today in 2025 your age is", age)

# Product of two numbers
x, y = input("Enter two numbers: ").split()
product = int(x) * int(y)
print("Product of " + x + " and " + y + " is " + str(product))

# BMI CALCULATOR
weight_in_kg = int(input("Enter your weight: "))
height_in_m = float(input("Enter your height: "))
bmi = weight_in_kg / (height_in_m ** 2)
print("YOUR BMI = " + str(round(bmi, 2)))