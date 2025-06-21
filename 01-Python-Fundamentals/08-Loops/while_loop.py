""" 
While loop - When you don't know how many times you have to repeat the task

- Do this again and again until a condition is false.
"""
## While loop with increasing value
i = 0
while (i < 3):
    print(i)
    i += 1

## While loop with decreasing value
print("")
count = 5
while (count > 0):
    print(count)
    count = count - 1

## Else with while loop
print("")
x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print("counter is 0")

# Another example
print("")
# Ask the user to guess the number
secret = 7
guess = 0

while guess != secret:
    guess = int(input("Guess the number: "))
    if guess != secret:
        print("Wrong! Try again.")
    
print("Correct guess!!!")