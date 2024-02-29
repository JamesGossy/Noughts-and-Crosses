
# Noughts and Crosses Game in Python

This Python script lets you play a classic game of Noughts and Crosses in the console. The game is designed for two players taking turns to mark spaces in a 3x3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

## Features

- **Simple Console Interface**: The game runs in the console, making it easy to play.
- **Two Player Game**: Alternating turns between 'X' and 'O'.
- **Input Validation**: Ensures that players can only make valid moves.
- **Win Detection**: Automatically detects and announces the winner.
- **Tie Detection**: Detects when the game is a tie, meaning the board is full and no player has won.

## How to Play

1. Run the script in a Python environment. Python 3 is recommended.
2. The game will prompt each player to enter their move by selecting a number from 1 to 9. Each number corresponds to a position on the board, as shown below:

  1|2|3  
  -+-+-
  4|5|6  
  -+-+-
  7|8|9  

3. Players take turns to input their moves. The game checks for a win or tie after each move.
4. When a player wins or the game is a tie, the final board state is displayed, and the game ends.

## Requirements

- Python 3.x

## Running the Game

To start the game, navigate to the directory containing the script and run:

python noughts_and_crosses.py

Enjoy the game, and may the best player win!

