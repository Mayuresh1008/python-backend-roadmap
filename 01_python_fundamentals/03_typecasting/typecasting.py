""" 
Typecasting in Python:
The conversion of one datatype into the other datatype is known as typecasting in python or type conversion in python.
"""

a = "1"
b = "2"
print(a + b)
# Using Typecasting
print(int(a) + int(b))

# Implicit Typecasing
c = 1.9
d = 8
print(c + d)

x = 10                  # int
y = 5.5                 # float
result = x + y          # Output:15.5 (float)
print(type(result))     # <class 'float'>

# Explicit Typecasting
# String to Number
num_str = "123"
num_int = int(num_str)
print(num_int * 2)

price = "99.99"
price_float = float(price)

# Number to String
age = 25
age_str = str(age)
print("I am " + age_str + " years old.")

# Boolean Conversion
print(bool(0)) # False
print(bool(1)) # True
print(bool("Y")) # True
print(bool("")) # False

""" 
When Type Casting Fails
print(int("Hello")) # ValueError(text can't become an int)
"""

# Check the string before converting to int
user_input = "123"
if user_input.isdigit():
    print(int(user_input)) # Safe!
else:
    print("Invalid Number!")
    
# Converting "3.14" to float
pi = "3.14"
pi_in_float = float(pi)
print(pi_in_float)
print(type(pi_in_float))

# Converting True to integer
num = True
num_as_int = int(num)
print(num_as_int)
print(type(num_as_int))

# printing str(100) + days using print statement
print(str(100) + " days.")

# Converting List to Tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)

# Converting Tuple of Pairs to Dictionary
items = [("a", 1), ("b", 2)]
items_dict = dict(items)
print(items_dict)