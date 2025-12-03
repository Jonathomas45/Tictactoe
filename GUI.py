import tkinter as tk  # importing gui creation tools

# an instant created with ".Tk()" while the instants named with text before the dot and all equaled to root
root = tk.Tk()
# name of instant(tk.Tk())'s window is TicTacToe
root.title("TicTacToe")
# Size of instant(tk.Tk())'s window is 500x500

# visible string
label = tk.Label(root, text="ARE YOU READY!", font=("Arial", 18))
label.pack()


class Button:
    turn = 1
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=90)

    def __init__(self, name, row, col):
        self.button = tk.Button(frame, command=self.click_button)
        self.button.grid(row=row, column=col, sticky=tk.W + tk.E)
        self.button.config(height=5, width=int(15))
        self.row = row
        self.column = col
        self.name = name
        self.text = self.button["text"]

    def click_button(self):
        turn = Button.turn
        if self.button["text"] == '' or "":
            if turn % 2 != 0:
                self.button.config(text='X')
                print(f'{self.name}+{turn}')
                self.text = 'X'
            elif turn % 2 == 0:
                self.button.config(text='O')
                print(f'{self.name}+{turn}')
                self.text = 'O'
            Button.turn += 1
            winning_condition()
        elif self.button["text"] != "":
            if turn == 9:
                winning_condition()
            elif turn == 10:
                print('Draw')
            else:
                print("Not your turn")
                print({turn})


def winning_condition():
    row0 = BT1.text + BT2.text + BT3.text
    row1 = BT4.text + BT5.text + BT6.text
    row2 = BT7.text + BT8.text + BT9.text
    column0 = BT1.text + BT4.text + BT7.text
    column1 = BT2.text + BT5.text + BT8.text
    column2 = BT3.text + BT6.text + BT9.text
    cross1 = BT1.text + BT5.text + BT9.text
    cross2 = BT3.text + BT5.text + BT7.text
    board = [row0, row1, row2, column0, column1, column2, cross1, cross2]
    print(board)
    x_win = "XXX"
    o_win = "OOO"

    for lines in board:
        if lines == x_win:
            winner = tk.Label(root, text="X wins", font=("Arial", 18))
            winner.pack()
        if lines == o_win:
            winner = tk.Label(root, text="O wins", font=("Arial", 18))
            winner.pack()


frame = Button.frame
# This is the button method
BT1 = Button('BT1', 0, 0)

BT2 = Button('BT2', 0, 1)

BT3 = Button('BT3', 0, 2)

BT4 = Button('BT4', 1, 0)

BT5 = Button('BT5', 1, 1)

BT6 = Button('BT6', 1, 2)

BT7 = Button('BT7', 2, 0)

BT8 = Button('BT8', 2, 1)

BT9 = Button('BT9', 2, 2)
buttons = [BT1, BT2, BT3, BT4, BT5, BT6, BT7, BT8, BT9]

root.mainloop()
