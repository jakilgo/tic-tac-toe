from Utilities import tictactoe
import sys

if __name__ == '__main__':
    play_first = sys.argv[1]
    if play_first == '1':
        turn = True
    else:
        turn = False
    app = tictactoe(turn)
    app.mainloop()
