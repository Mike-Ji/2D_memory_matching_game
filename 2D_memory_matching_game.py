import tkinter as tk
import random
from tkinter import messagebox
import time

class Tile:
    def __init__(self, parent):
        self.parent = parent
        self.buttons = [[tk.Button(root,\
                                   width = 4, height = 2,\
                                   command=lambda row=row, column=column: \
                                   self.choose_tile(row, column)\
                                   ) for column in range(4)] for row in range(4)]

        # put the buttons on the grid
        for row in range(4):
            for column in range(4):
                self.buttons[row][column].grid(row=row, column=column)
        self.first = None
        self.set_board()


    def set_board(self):
        self.answer = list('AABBCCDDEEFFGGHH')
        random.shuffle(self.answer)
        self.answer = [self.answer[:4],
                       self.answer[4:8],
                       self.answer[8:12],
                       self.answer[12:]]

        for row in self.buttons:
            for button in row:
                button.config(text='', state=tk.NORMAL)

        self.start_time = time.monotonic()
    
        
    def choose_tile(self, row, column):
        self.buttons[row][column].config(text=self.answer[row][column])
        self.buttons[row][column].config(state=tk.DISABLED)
        if not self.first:
            self.first = (row, column)
        else:
            a,b = self.first
            if self.answer[row][column] == self.answer[a][b]:
                self.answer[row][column] = ''
                self.answer[a][b] = ''
                if not any(''.join(row) for row in self.answer):
                    duration = time.monotonic() - self.start_time
                    messagebox.showinfo(title="Success!", message="You win! \
Time: {:.2f}".format(duration))
                    self.parent.after(5000, self.set_board)
            else:
                self.parent.after(1000, lambda: self.hide_tiles(row, column, a, b)) 

            self.first = None
            

    def hide_tiles(self, x1, y1, x2, y2):
        self.buttons[x1][y1].config(text='',state=tk.NORMAL)
        self.buttons[x2][y2].config(text='',state=tk.NORMAL)


root = tk.Tk()
tile = Tile(root)
root.mainloop()

