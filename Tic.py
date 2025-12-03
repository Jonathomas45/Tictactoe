import tkinter as tk
import random


root = tk.Tk()

root.title("TicTacToe")

root.geometry("500x250")
label = tk.Label(root, text="ARE YOU READY!", font=("Arial", 18))
label.pack()

textbox = tk.Text(root, height=1, font=("Arial", 12))
textbox.pack()

textboxframe = tk.Frame(root)
textboxframe.columnconfigure(0, weight=1)
textboxframe.columnconfigure(1, weight=1)
textboxframe.columnconfigure(2, weight=1)

# this is the input style
txtbox1 = tk.Text(textboxframe, height=3, width=3, font=("Arial", 12))
txtbox1.grid(row=0, column=0, sticky=tk.W+tk.E)

txtbox2 = tk.Text(textboxframe, height=3, width=3, font=("Arial", 12))
txtbox2.grid(row=0, column=1, sticky=tk.W+tk.E)

txtbox3 = tk.Text(textboxframe, height=3, width=3, font=("Arial", 12))
txtbox3.grid(row=0, column=2, sticky=tk.W+tk.E)

txtbox4 = tk.Text(textboxframe, height=3, width=3, font=("Arial", 12))
txtbox4.grid(row=1, column=0, sticky=tk.W+tk.E)

txtbox5 = tk.Text(textboxframe, height=3, width=3, font=("Arial", 12))
txtbox5.grid(row=1, column=1, sticky=tk.W+tk.E)

txtbox6 = tk.Text(textboxframe, height=3, width=3, font=("Arial", 12))
txtbox6.grid(row=1, column=2, sticky=tk.W+tk.E)

txtbox7 = tk.Text(textboxframe, height=3, width=3, font=("Arial", 12))
txtbox7.grid(row=2, column=0, sticky=tk.W+tk.E)

txtbox8 = tk.Text(textboxframe, height=3, width=3, font=("Arial", 12))
txtbox8.grid(row=2, column=1, sticky=tk.W+tk.E)

txtbox9 = tk.Text(textboxframe, height=3, width=3, font=("Arial", 12))
txtbox9.grid(row=2, column=2, sticky=tk.W+tk.E)

textboxframe.pack()




root.mainloop()