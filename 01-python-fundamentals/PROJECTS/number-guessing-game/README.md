# 🎯 Number Guessing Game

A simple Python game where the computer picks a random number, and you have to guess it with hints provided after each attempt.

---

## ✅ Features
- The computer randomly selects a number between **1 and 100**.
- You can keep guessing until you find the correct number.
- Hints:
  - **Too High** → Your guess is greater than the secret number.
  - **Too Low** → Your guess is smaller than the secret number.
- Displays the number of attempts taken to guess correctly.

---

## 📂 Project Structure
'''yaml

number\_guessing\_game/
│
├── number\_guessing\_game.py   # Main Python script
└── README.md                 # Project documentation
'''

---

## ▶️ How to Run the Game
1. Make sure Python is installed on your system.
2. Clone or download this project.
3. Open a terminal in the project folder.
4. Run the script:
   ```bash
   python number_guessing_game.py
```

---

## 🧠 How the Game Works

1. The computer picks a random number between 1 and 100 using:

   ```python
   random.randint(1, 100)
   ```
2. You enter your guess.
3. The game tells you:

   * **Too High** → Lower your guess.
   * **Too Low** → Increase your guess.
4. Once you guess correctly, the game shows how many attempts you took.

---

## 📌 Example Output

```
Guess the number: 50
Too High
Guess the number: 25
Too Low
Guess the number: 37
You guessed the correct number 37 in 3 attempts.
```

---


