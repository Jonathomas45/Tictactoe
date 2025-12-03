import tkinter as tk
int = 0


class CounterButton:
    def __init__(self, text, row, column):
        self.count = 0
        self.button = tk.Button(root, text=text, command=self.count_up)
        self.button.grid(row=row, column=column, sticky=tk.W + tk.E)

    def count_up(self):
       self.count += 1
       self.button.config(text=f"Count: {self.count}")

root = tk.Tk()
root.title("Run Executable Example")
root.geometry("500x250")

button = CounterButton("Nope ", 0, 0)
button2 = CounterButton(" ", 0, 1)
root.mainloop()




