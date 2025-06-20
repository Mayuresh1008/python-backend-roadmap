## If statement
age = 18 
if age >= 18:
    print("You can vote!\n")

## If-Else Statement
age = int(input("Enter your age: "))
print("Your age is:", age)

if age >= 18:
    print("You can drive")
else:
    print("You can not drive")

print("")

# Another example
applePrice = 210
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")
    
# One more example
print("")
temperature = 25
if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too hot")

print("")
## Elif Statement
num = int(input("Enter a number:"))
if (num < 0):
    print("Number is negative")
elif (num > 0):
    print("Number is positive")
else:
    print("Number is zero")
    
# Another example 
score = 85
print("")
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D")

