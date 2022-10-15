from math import inf
import tkinter as tk
from tkinter import *
from tkinter.font import Font
from alphabeta import alphabeta
from secrets import choice


class buttonStyle(tk.Button):
    won = False
    def __init__(self, window, pos):
        super().__init__(master=window)
        self.pos = pos
        self["command"] = lambda: self.button_clicked(window, pos)
        self['text'] = ''
        self['width'] = 2
        self['height'] = 1
        self['fg'] = 'black'
        self['disabledforeground'] = 'black' #ensures colors stay normal when disabled
        self['highlightbackground'] = "grey"
        self['highlightthickness'] = 1
        
        font = Font(size=133)
        self['font'] = font
        
    def get_pos(self):
        return self.pos
    
    def button_clicked(self, window, pos, AI = None):
        if not buttonStyle.won:
            placement = window.get_turn()
            self['text'] = placement
            self['state'] = DISABLED
            window.update_value(pos,placement)
            if (window.board.check_winner()[0]):
                print(window.board.board)
                window.draw_winner()
                print(placement + ' wins!')
                buttonStyle.won = True
                window.after(1500, window.display_winner)
                return
            if len(window.board.get_empty()) == 0:
                print(window.board.board)
                print ("Tie!")
                window.after(1500, window.display_draw)
                return
            
            if AI == None:
                window.AI_click(alphabeta(0,window.board, window.play_as_AI, True, -inf, inf))
              
            

class tictactoeBoard:
    def __init__(self,board, play, AI):
        self.board = board
        self.play = play
        self.AI = AI
        
    def update_board(self, pos, play):
        self.board[pos[0]][pos[1]] = play
    
    def get_board(self):
        return self.board
    
    def get_play(self):
        if self.play:
            return 'X'
        else:
            return 'O'
    
    def get_empty(self):
        empties = []
        for i_key, i_value in enumerate(self.board):
            for j_key, j_value in enumerate(i_value):
                if j_value == None:
                    empties.append((i_key,j_key))
        return empties
    
    def check_winner(self):
        for i_key, i_value in enumerate(self.board):
           if (i_value[0] == i_value[1] == i_value[2]):
               if i_value[0] == 'X':
                   return True, 'X'
               elif i_value[0] == 'O':
                   return True, 'O'
           if (self.board[0][i_key] == self.board[1][i_key] == self.board[2][i_key]):
               if self.board[0][i_key] == 'X':
                   return True, 'X'
               if self.board[0][i_key] == 'O':
                   return True, 'O'
        if (self.board[0][0] == self.board[1][1] == self.board[2][2]):
            if self.board[1][1] == 'X':
                return True, 'X'
            if self.board[1][1] == 'O':
                return True, 'O'
        if (self.board[0][2] == self.board[1][1] == self.board[2][0]):
            if self.board[1][1] == 'X':
                return True, 'X'
            if self.board[1][1] == 'O':
                return True, 'O'
            
        return False, None

class tictactoe(tk.Tk):
    def __init__(self, turn):
        super().__init__()
        
        
        if not turn:
            self.play_as_AI = 'X'
            self.turn = turn
            pos = choice([(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)])
              
        else:
            self.play_as_AI = 'O'
            self.turn = not turn
            pos = (-1,-1)

        self.board = tictactoeBoard([[None,None,None],[None,None,None],[None,None,None]], turn, self.play_as_AI) #create empty board
        self.visual_setup(pos)


    
    def get_board(self):
        return self.board
    
    def visual_setup(self, pos):
        self.title("Tic-Tac-Toe: AlphaBeta")
        self.configure(bg='black')
        
        #set size and position board
        width = 498
        height = 485
        x = int(self.winfo_screenwidth()/2 - width/2)
        y = int(self.winfo_screenheight()/2 - height/2)
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.minsize(width,height)
        self.maxsize(width,height)
        
        #create board visually
        for i in range(3):
            for j in range(3):
                button = buttonStyle(self, (i,j))
                button.grid(row=i,column=j)
                if (i,j) == pos:
                    placement = self.get_turn()
                    button['text'] = placement
                    button['state'] = DISABLED
                    self.update_value(pos,placement)
                                
    def get_turn(self):
        self.turn = not self.turn
        if self.turn:
            return 'X'
        else:
            return 'O'
    
    def update_value(self, pos, x_or_o):
        self.board.update_board(pos, x_or_o)
        
    def AI_click(self, pos):
        for widget in self.winfo_children():
            if widget.get_pos() == pos[0]:
                widget.button_clicked(self, pos[0], 'AI')
    
    def draw_winner(self):
        for widget in self.winfo_children():
            widget['state'] = DISABLED
    
    def display_winner(self):
        l = Label(self, text='', bg = 'dark gray', height = self.winfo_height(), width = self.winfo_width(), fg = 'red', font = Font(size = 50))
        if self.turn:
            l['text'] = 'X wins!'
        else:
            l['text'] = 'O wins!'
        l.place(x=self.winfo_width()/2, y=self.winfo_height()/2, anchor="center")
        self.after(2500, self.destroy)

    def display_draw(self):
        l = Label(self, text='', bg = 'dark gray', height = self.winfo_height(), width = self.winfo_width(), fg = 'red', font = Font(size = 50))
        l['text'] = 'It\'s a draw!'
        l.place(x=self.winfo_width()/2, y=self.winfo_height()/2, anchor="center")
        self.after(2500, self.destroy)
