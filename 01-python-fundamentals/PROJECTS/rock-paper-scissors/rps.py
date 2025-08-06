import random
import sys

let_continue = True

print("********* WELCOME TO THE GAME *************")
print("--- ROCK ------ PAPER ------ SCISSORS ----")
print("Press - \n1 for ROCK, \n2 for PAPER, \n3 for SCISSORS,")
while let_continue:
    student_choice = int(input("\nEnter your choice: "))
    print(student_choice)
    computer_choice = int(random.choice("123"))
    print(computer_choice)
    if student_choice < 1 or student_choice > 3:
        sys.exit("Invalid input!!")
    elif (
        (student_choice == 1 and computer_choice == 3)
        or (student_choice == 2 and computer_choice == 1)
        or (student_choice == 3 and computer_choice == 2)
    ):
        print("\nYOU WIN!!!!")
    elif student_choice == computer_choice:
        print("\nTIE GAME")
    else:
        print("\nCOMPUTER WINS")

    repeat = input("\nDo you want to play again:\n Y for yes and N for no: ").lower()
    if repeat == "n":
        let_continue = False
        print("\n_________ THANK YOU FOR PLAYING __________")
    elif repeat != "y" and "n":
        sys.exit("\nERROR!, You entered the wrong input.\nSYSTEM HANGED!!!")
