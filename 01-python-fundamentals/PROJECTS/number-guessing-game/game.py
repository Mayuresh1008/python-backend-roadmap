import random

secret_number = random.randint(1, 100)

correct = False
attempts = 0

while not correct:
    guess = int(input("Guess the number:"))
    attempts += 1

    if guess == secret_number:
        print(f"You guessed the correct number {secret_number} in {attempts} attempts.")
        correct = True
    elif guess > secret_number:
        print("Too High")
    elif guess < secret_number:
        print("Too Low")
    else:
        print("Invalid input")
