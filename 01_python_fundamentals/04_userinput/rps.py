""" 
This is a practice file of practicing user input in python,
In this file i am making a rock, paper and scissors game 
and using the concepts like user input, random module in python and so on.
"""
import sys
import random

print("")
playerchoice = input("Enter...\n1 for Rock\n2 for Paper, or \n3 for Scissors:\n\n")

player = int(playerchoice)

if player < 1 | player > 3:
    sys.exit("You must enter 1, 2, or 3.")

computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("You chose " + playerchoice + ".")
print("Python chose " + computerchoice + ".")
print("")

if player == 1 and computer == 3:
    print("You win!")
elif player == 2 and computer == 1:
    print("You win!")
elif player == 3 and computer == 2:
    print("You win!")
elif player == computer:
    print("Tie Game!")
else:
    print("Python wins!")
