# Tic Tac Toe 🎮

A command-line Tic Tac Toe game built in Python as my second project, after a CLI number guessing game. Available in two versions.

---

## Versions

### 1. Human vs Human (`cli/ttt_(human_v_human).py`)
Two human players take turns on the same machine.

### 2. Human vs Computer (`cli/ttt_(human_vs_comp).py`)
Play against a computer opponent that makes moves using the random module. The computer always plays as `o`.

---

## How to Run

Make sure you have Python 3 installed, then:

```bash
# Human vs Human
python cli/ttt_human_v_human.py

# Human vs Computer
python cli/ttt_human_vs_comp.py
```

---

## How to Play

- Enter your name and symbol when prompted (e.g. `nitin,x`)
- The board positions are numbered 1-9:

```
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
```

- Enter a number (1-9) to place your symbol on that cell
- Enter `0` to quit at any time

---

## Features

1.Turn-based gameplay
2.Win detection for rows, columns, and diagonals
3.Invalid move handling — can't place on an occupied cell
4.Invalid input handling — non-integer inputs are caught
5.Draw detection when the board is full
6.Symbol validation — `o` is reserved for the computer in the "vs computer" version
7.Random computer opponent with collision handling

---

## Project Structure

```
tic-tac-toe/
│
├── cli/
│   ├── ttt_human_v_human.py
│   └── ttt_human_vs_comp.py
│
└── README.md
```

---

## What I Learned

- OOP with classes and instance attributes
- 2D list manipulation
- `divmod` and `//` `%` for coordinate mapping
- `global` variables and mutability in Python
- Recursive input validation
- `enumerate`, `join`, list comprehensions
- `try/except ValueError` for input handling

---

## Upcoming

- GUI version using tkinter
