""" 
Built-in functions are predefined functions that come with python
you don't need to install or import anything

They help us to:
Take input - input()
print output - print()
do math - abs(), round(), pow(x, y), max(), min(), sum()
work with data - len(), sorted(), reversed(), enumerate(), zip(), strip(), rstrip(), lstrip()
debug your code - id(), help(), dir(), eval()
type conversion - int(), float(), str(), bool(), list(), tuple()
type checking - type(), isinstance()

"""

## Input/Output Functions

# print() - Show output

print("Hello, world!")

# input() - Take user input
name = input("Enter your name: ")
print("Hello", name)

print("")

## Type Conversion Functions

num = "10"
print(int(num) + 5)

print("")

## Type Checking Functions

x = 5.5
print(type(x))
print(isinstance(x, int))
print(isinstance(x, float))

print("")

## Math Function

print(abs(-9))
print(round(3.14159, 2))
print(pow(2, 3))

print("")

## Data/Sequence Functions
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
    
print("")

## Debug/Utility Functions
a = 10
print(id(a))

# help(str)

print("\n\n")

## Example : Combine Multiple Built-in Functions

name = input("Enter your name: ").strip().title()
print("Hello", name)
print("Name length:", len(name))