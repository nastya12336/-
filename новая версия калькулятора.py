import tkinter as tk
from tkinter import messagebox
import math
import  random


def calculate():
    var = opt.get()
    if var == "Сложить":
        plus()
    elif var == "Вычесть":
        minus()
    elif var == "Умножить":
        multi()
    elif var == "Делить":
        div()
    elif var == "Факториал":
        factorial()
    elif var == "Синус":
        sinus()
    elif var == "Косинус":
        cosinus()


def plus():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        label_res.config(text=f'Результат: {result}')
    except:
        messagebox.showerror('Ошибка', 'Введите числа')


def minus():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 - num2
        label_res.config(text=f'Результат: {result}')
    except:
        messagebox.showerror('Ошибка', 'Введите числа')


def multi():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        label_res.config(text=f'Результат: {result}')
    except:
        messagebox.showerror('Ошибка', 'Введите числа')


def div():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            messagebox.showerror('Ошибка', 'Деление на ноль!')
            return
        result = num1 / num2
        label_res.config(text=f'Результат: {result:.4f}')
    except:
        messagebox.showerror('Ошибка', 'Введите числа')


def factorial():
    try:
        num = int(entry1.get())
        if num < 0:
            messagebox.showerror('Ошибка', 'Факториал определен только для неотрицательных чисел')
            return
        result = math.factorial(num)
        label_res.config(text=f'Факториал {num}! = {result}')
    except:
        messagebox.showerror('Ошибка', 'Введите целое число для факториала')


def sinus():
    try:
        angle = float(entry1.get())
        answer = messagebox.askyesno("Единицы измерения",
                                     "Угол в градусах? (Да=градусы, Нет=радианы)")

        if answer:  # Если градусы
            angle_rad = math.radians(angle)
            result = math.sin(angle_rad)
            label_res.config(text=f'sin({angle}°) = {result:.6f}')
        else:  # Если радианы
            result = math.sin(angle)
            label_res.config(text=f'sin({angle:.4f} рад) = {result:.6f}')
    except:
        messagebox.showerror('Ошибка', 'Введите число')


def cosinus():
    try:
        angle = float(entry1.get())
        answer = messagebox.askyesno("Единицы измерения",
                                     "Угол в градусах? (Да=градусы, Нет=радианы)")

        if answer:  # Если градусы
            angle_rad = math.radians(angle)
            result = math.cos(angle_rad)
            label_res.config(text=f'cos({angle}°) = {result:.6f}')
        else:  # Если радианы
            result = math.cos(angle)
            label_res.config(text=f'cos({angle:.4f} рад) = {result:.6f}')
    except:
        messagebox.showerror('Ошибка', 'Введите число')

def mouse_left_on_click(event):
    color = '#' + '{:06x}'.format(random.randint(0,16777216))
    root['bg'] = color


def mouse_right_on_click(event):
    entry_frame2.pack_forget()


def change_frames(*args):
    flag = opt.get()
    entry_frame1.pack_forget()
    entry_frame2.pack_forget()
    if flag in values[0:4]:
        entry_frame1.pack(pady=5)
        entry_frame2.pack(pady=5)
    elif flag in values[4:]:
        entry_frame1.pack(pady = 5)


root = tk.Tk()
root.geometry("500x500")
root.title("Калькулятор")

entrys_frame = tk.Frame(root)
entrys_frame.pack(pady = 10)

# Первое значение
entry_frame1 = tk.Frame(entrys_frame)


label1 = tk.Label(entry_frame1, text="Значение 1:")
label1.pack(side=tk.LEFT, padx=5)

entry1 = tk.Entry(entry_frame1)
entry1.pack(side=tk.LEFT)

# Второе значение
entry_frame2 = tk.Frame(entrys_frame)


label2 = tk.Label(entry_frame2, text="Значение 2:")
label2.pack(side=tk.LEFT, padx=5)

entry2 = tk.Entry(entry_frame2)
entry2.pack(side=tk.LEFT)

# Панель операций
res_frame = tk.Frame(root)
res_frame.pack(pady=20)

values = ["Сложить", "Вычесть", "Умножить", "Делить", "Факториал", "Синус", "Косинус"]
opt = tk.StringVar(value="Сложить")
opt.trace('w', change_frames)

# Выпадающий список
combo = tk.OptionMenu(res_frame, opt, *values)
combo.pack(side=tk.LEFT, padx=5)

# Кнопка расчета - ВАЖНО: создаем ПРАВИЛЬНО
calc_button = tk.Button(res_frame,
                        text="Посчитать",
                        command=calculate,  # Это обязательно!
                        bg="#2E8B57",
                        fg="white",
                        font=('Arial', 11, 'bold'),
                        relief=tk.RAISED,
                        borderwidth=3,
                        cursor="hand2",
                        padx=20)
calc_button.pack(side=tk.LEFT, padx=5)

# Результат
label_res = tk.Label(root, text="Результат: ", font=('Arial', 12))
label_res.pack(pady=20)

root.bind('<Button-1>', mouse_left_on_click)
root.bind('<Button-2>', mouse_right_on_click)

root.mainloop()
