# 🎮 Rock-Paper-Scissors Game

A simple Python console-based game where you play **Rock-Paper-Scissors** against the computer.

---

## ✅ Features
- Player chooses **Rock**, **Paper**, or **Scissors**.
- Computer randomly selects one of the three options.
- Rules:
  - Rock beats Scissors
  - Scissors beats Paper
  - Paper beats Rock
- Displays the winner or tie.
- Option to play multiple rounds.

---

## 📂 Project Structure

````
rock\_paper\_scissors/
│
├── rock\_paper\_scissors.py   # Main Python script
└── README.md                # Project documentation

````


## ▶️ How to Run the Game
1. Make sure Python is installed on your system.
2. Clone or download this project.
3. Open a terminal in the project folder.
4. Run the script:
   ```
   python rock_paper_scissors.py
```

---

## 🧠 How the Game Works

1. The game welcomes you and shows the options:

   * `1` → Rock
   * `2` → Paper
   * `3` → Scissors
2. Player inputs their choice.
3. Computer picks a random choice using:

   ```python
   random.choice("123")
   ```
4. Compare both choices:

   * If Player beats Computer → **YOU WIN**
   * If Computer beats Player → **COMPUTER WINS**
   * If both same → **TIE GAME**
5. Ask player if they want to play again:

   * `Y` → Play another round.
   * `N` → Exit the game.
6. Invalid inputs exit the game with an error message.

---

## 📌 Example Output

```
********* WELCOME TO THE GAME *************
--- ROCK ------ PAPER ------ SCISSORS ----
Press -
1 for ROCK,
2 for PAPER,
3 for SCISSORS,

Enter your choice: 1
1
2

COMPUTER WINS

Do you want to play again:
 Y for yes and N for no: y
```




