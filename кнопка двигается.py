import tkinter as tk
from tkinter import messagebox
import math
import  random

root = tk.Tk()
root.geometry("500x500")
root.title("Калькулятор")
def jump(*args):
    x=random.randint(0,300)
    y = random.randint(0,400)
    btn1.place(x=x, y=y)
def info():
    messagebox.showinfo("Оценка", "не повезло")
btn1 = tk.Button(text = 'пять', bg = 'green')
btn1.place(x=20,y=20)
btn2=tk.Button(text='два', command = info, bg = 'red')
btn2.place(x=100,y=20)
btn1.bind('<Motion>', jump)
root.mainloop()
