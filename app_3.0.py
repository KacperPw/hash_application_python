
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
    button5.destroy()

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


def code(txt):
    cesars_coded = " "
    for i in range(len(txt)):
        if ord(txt[i]) > 122 - 3:
            cesars_coded += chr(ord(txt[i]) + 3 - 26)
        else:
            cesars_coded += chr(ord(txt[i]) + 3)
    return cesars_coded


def cesar_code():
    data_to_code = entry1.get()
    code_data = code(data_to_code)
    label3 = tk.Label(root, text=code_data)
    label3.pack()


def open_cezar_code():
    button1.destroy()
    button2.destroy()
    button5.destroy()

    label2 = tk.Label(root, text="Enter data to code")
    label2.pack()
    entry1.pack()
    button_cesar = tk.Button(root, text="Code", command=cesar_code)
    button_cesar.pack()
    exit_button = tk.Button(root, text="exit", command=exit)
    exit_button.pack()


button3 = tk.Button(root, text="hash", command=hashing_data)

button5 = tk.Button(root, text="Open cezar code app", command=open_cezar_code)
button5.pack()

button1 = tk.Button(root, text="Open hash app", command=open_app)
button1.pack()

button2 = tk.Button(root, text="Exit", command=exit)
button2.pack()


root.mainloop()
