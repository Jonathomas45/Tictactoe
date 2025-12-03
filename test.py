import tkinter as tk


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("TicTacToe")

        self.x_turn = True  # X starts first

        # Using grid for the label
        self.label = tk.Label(root, text="ARE YOU READY!", font=("Arial", 18))
        self.label.grid(row=0, column=0, columnspan=3, pady=10)

        # Using grid for the textbox
        self.textbox = tk.Text(root, height=1, font=("Arial", 12))
        self.textbox.grid(row=1, column=0, columnspan=3, pady=10)

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text=" ", font=("Arial", 24), width=5, height=2,
                                   command=lambda row=i, col=j: self.button_click(row, col))
                button.grid(row=i+2, column=j, sticky=tk.W + tk.E)  # Start buttons from row 2
                self.buttons[i][j] = button

    def button_click(self, row, col):
        if self.buttons[row][col]["text"] == " ":
            if self.x_turn:
                self.buttons[row][col]["text"] = "X"
            else:
                self.buttons[row][col]["text"] = "O"

            self.x_turn = not self.x_turn  # Switch turns

            # Here you can add more logic to check for a winner or draw
            # Example: check_winner()


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
