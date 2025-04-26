# Number Guessing Game 🎯

This is a simple Number Guessing Game implemented in Python.  
The program randomly selects a number within a user-defined range, and you have to guess the number in the minimum number of attempts possible (calculated using binary search logic).

---

## ✨ Features

- User specifies the start and end of the range.
- The program randomly selects a number within the given range.
- Minimum number of guesses required is calculated using binary search principle (`log₂(range size)`).
- After each guess, the user receives feedback:
  - Whether the guess is **too high** or **too low**.
  - If the guess is correct, the program **congratulates** the user and displays the number of attempts taken.
  - If the user fails to guess within the minimum number of attempts, the correct answer is revealed.

---

## 🛠 Requirements

- Python 3.x
- numpy

---

## 🚀 How to Run

1. **Install numpy** (if not already installed):

   ```bash
   pip install numpy


2. **Save the code to a file**, for example:

    number_guessing_game.py


3. **Follow the prompts:**

    Enter the start and end of the range.

    Try to guess the number within the allowed number of attempts!

