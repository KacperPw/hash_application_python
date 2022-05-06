import tkinter as tk
from tkinter import *
import bcrypt


root = tk.Tk()
root.geometry("480x480")

label1 = tk.Label(root, text="Enter data to hash")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()


def btnfunc():

    data_to_hash = entry1.get().encode("utf-8")

    hashed_data = bcrypt.hashpw(data_to_hash, bcrypt.gensalt())

    label2 = tk.Label(root, text=hashed_data)
    label2.pack()


btn1 = tk.Button(root, text="Im button", command=btnfunc)
btn1.pack()


root.mainloop()
