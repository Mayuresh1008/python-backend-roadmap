""" 
Do-while Loop:
That loop where the code runs at least once before checking the condition

Python has no built-in do while loop but we can emulate it using a while True + break
"""

# Python Emulated do-while Example:
# Example : Ask password until correct

while True:
    password = input ("Enter the password:")
    
    if password == "python123":
        print("Access granted!!!")
        break # condition met, exit loop
    else:
        print("Wrong password, Try again!!")
    
# Another Example : Keep adding numbers until 0 is entered
while True:
    num = int(input("Enter a number (0 to stop): "))
    
    if num == 0:
        print("Loop ended")
        break
    
    print(f"You entered: {num}")

""" 
Trick Template We can use 
while True:
    # your code that should run at least once
    
    if not condition:
        break
"""