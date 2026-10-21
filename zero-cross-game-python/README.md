# Zero Cross Game Using Python

A command-line **Zero Cross (Tic-Tac-Toe)** game where you play against a computer opponent powered by the **Minimax algorithm**.

## Features
- Player vs Computer gameplay
- Minimax-based computer moves
- Win, loss, and draw detection
- Input validation for invalid or occupied positions
- No third-party packages required

## Requirements
- Python 3.8 or newer (standard library only)

## Run the game
1. Download or clone this repository.
2. Open a terminal in this folder.
3. Run:

```bash
python zero_cross.py
```

On some systems, use `python3 zero_cross.py`.

## How to play
- You play as **X** and the computer plays as **O**.
- The board positions are numbered 1 through 9.
- Enter an available position when prompted.
- Three matching symbols in a row, column, or diagonal wins.
- If all squares fill and nobody wins, the game is a draw.

## How the AI works
Minimax recursively evaluates available moves and their possible outcomes. The computer maximizes its score while assuming the player will choose moves that minimize it. It scores wins, losses, and draws, with a preference for faster wins and slower losses. With the implementation used here, the computer plays optimally for standard Tic-Tac-Toe.

## Concepts practiced
- Python functions and loops
- Lists and board-state representation
- Conditions and input validation
- Game-state evaluation
- Recursion and the Minimax search algorithm

## Future improvements
- Add a graphical interface with Tkinter or Pygame
- Add difficulty levels
- Add score tracking and replay options

## Author
**Pankaj Kumar** — BCA student specializing in Data Science.

## License
Available for educational and personal learning use. Add an MIT LICENSE file if you wish to distribute it under the MIT License.
