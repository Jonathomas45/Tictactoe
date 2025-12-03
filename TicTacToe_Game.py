import tkinter as tk  # importing gui creation tools

# an instant created with ".Tk()" while the instants named with text before the dot and all equaled to root
root = tk.Tk()
# name of instant(tk.Tk())'s window is TicTacToe
root.title("https://github.com/Jonathomas45/TicTacToe")

# visible string
label = tk.Label(root, text="TicTacToe", font=("Arial", 18))
label.pack()


scorer = tk.Label(root, text="", font=("Arial", 20))
scorer.pack()

class Game:
    turn = 1
    frame = tk.Frame(root)
    def __init__(self, name, row, col):
        frame.pack(padx=5, pady=6)
        self.button = tk.Button(frame, command=self.click_button)
        self.button.grid(row=row, column=col, sticky="nsew")
        self.button.config(height=5, width=8, font=("Arial", 20))
        self.row = row
        self.column = col
        self.name = name
        self.text = self.button["text"]
        
    def click_button(self):
        turn = Game.turn
        if self.button["text"] == "":
            if turn % 2 != 0:
                self.button.config(text='X')
                print(f'{self.name}+{turn}')
                self.text = 'X'
            elif turn % 2 == 0:
                self.button.config(text='O')
                print(f'{self.name}+{turn}')
                self.text = 'O'
            winning_condition()
            Game.turn += 1
        if turn == 9 and scorer['text'] == "":
            scorer.config(text="Draw")
            scorer.pack()
    
def restart():
    for bt in buttons:
        bt.button.config(text='')  
        bt.text = ""               

    scorer.config(text='')
    Game.turn = 1



def winning_condition():
# I dont like how chunky this is there has to be a way to clean this up and simpify it
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

    scorer.config(text= "")
    for i, line in enumerate(board):
        if line == "X" * 3 or line == "O" * 3 in board:
            t =f"{board[i][0]} Wins"
            scorer.config(text= t)
            scorer.pack()
            return True

    
frame = Game.frame
# This is the button method
BT1 = Game('BT1', 0, 0)

BT2 = Game('BT2', 0, 1)

BT3 = Game('BT3', 0, 2)

BT4 = Game('BT4', 1, 0)

BT5 = Game('BT5', 1, 1)

BT6 = Game('BT6', 1, 2)

BT7 = Game('BT7', 2, 0)

BT8 = Game('BT8', 2, 1)

BT9 = Game('BT9', 2, 2)
buttons = [BT1, BT2, BT3, BT4, BT5, BT6, BT7, BT8, BT9]

   
        

reset = tk.Button(root, text="Restart", command= restart)
reset.pack()


root.mainloop()
