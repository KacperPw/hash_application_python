from cProfile import label
import tkinter as tk
from tkinter import *
import bcrypt


root = tk.Tk()

root.geometry("480x480")


entry1 = tk.Entry(root)

button4 = tk.Button(root, text="Exit", command=exit)


def open_app():
    button1.destroy()
    button2.destroy()

    label1 = tk.Label(text="Enter data to hash")
    label1.pack()

    entry1.pack()
    button3.pack()
    button4.pack()


def hashing_data():
    data_to_hash = entry1.get().encode("utf-8")
    hashed_data = bcrypt.hashpw(data_to_hash, bcrypt.gensalt())

    label2 = tk.Label(root, text=hashed_data)
    label2.pack()


button3 = tk.Button(root, text="hash", command=hashing_data)


button1 = tk.Button(root, text="Open hash app", command=open_app)
button1.pack()

button2 = tk.Button(root, text="Exit", command=exit)
button2.pack()


root.mainloop()
