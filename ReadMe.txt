To play, type the following phrase into the command line (assuming you are in the Tic-Tac-Toe directory)

For Minmax.py:
    python3 Minmax/Main.py X
For alphabeta.py:
    python3 alphabeta/Main.py X

For both, the 'X' represents the order you would like to play in (X always goes first)
To play as X (play first), substitute a '1' for X. EX: python3 Minmax/Main.py 1
To play as O (play second), substitute a '2' for X. EX: pythonn3 Minmax/Main.py 2

Next, the tic-tac-toe board will appear in a separate window. If you selected to play second, the board will have a random tile filled in to substitute the AI's initial move.
To play your piece, select the tile you would like to fill in. The AI will play automatically and you can then play your next turn

Once the game ends, the winner (or if its a draw) will be displayed (both on the separate window and command line).
The final game board will also be printed

Imports:
math: inf - allows to use infinity when initially calling minimax/alphabeta
tkinter - GUI, handles the buttons, frames, etc.
secrets: choice - random initial move for the AI (when it goes first)
sys - allows command line input to be read

Note:
Depth is used so that the AI will try to win as soon as it can rather making a move that still guarantees a win, but on a later move.
For example, the following board:
X | O | X
  | O | 
  |   | X
Since the sixth position (2nd row, last column) would be found first in the tree, the Minimax algorithm will select the first first move that guarantees a win.
Playing 'O' in the sixth position still guarantees a win on the following move, but by including depth we can give more weight to moves that result in a win sooner.
Depth is used in both algorithms, without it they would still work and play correctly, but including it ensures a win sooner rather than later.