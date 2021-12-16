from math import sqrt

def solver(a,b,c):
    # Решает квадратное уравнение и выводит ответ
    # находим дискриминант
    D = b*b - 4*a*c
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        text = "Дискриминант(D) равен %s \n X1 = %s \n X2 = %s \n" % (D, x1, x2)
    else:
        text = "Дискриминант(D) равен %s \n Это уравнение не имеет решений" % D
    return text

def inserter(value):
    # Вставить указанное значение в текстовый виджет
    output.delete("0.0","end")
    output.insert("0.0",value)

def handler():
    # Получить содержимое записей и передать результат в область вывода
    try:
        a_val = float(a.get())
        b_val = float(b.get())
        c_val = float(c.get())
        inserter(solver(a_val, b_val, c_val))
    except ValueError:
        inserter("Убедитесь, что вы ввели 3 числа")

# GUI Программы:

from tkinter import *

# главный элемент
root = Tk()
# иконка приложения
root.iconbitmap('x2.ico')
# устанавливаем название окна
root.title("ПО для решения квадратных уравнений")
# устанавливаем минимальный размер окна
root.geometry('389x240')
# выключаем возможность изменять окно
root.resizable(width=False, height=False)
# прозрачность окна(необязательно)
root.wm_attributes('-alpha', 0.99)
# создаем рабочую область
frame = Frame(root)
frame.grid()

# поле для ввода первого аргумента (a)
a = Entry(frame, width=5)
a.grid(row=1, column=1, padx=(10, 0))

# текст после первого аргумента
a_lab = Label(frame, text="x^2 +").grid(row=1, column=2)

# поле для ввода второго аргумента (b)
b = Entry(frame, width=5)
b.grid(row=1, column=3)
# текст после второго аргумента
b_lab = Label(frame, text="x +").grid(row=1, column=4)

# поле для ввода третьего аргумента (с)
c = Entry(frame, width=5)
c.grid(row=1, column=5)
# текст после третьего аргумента
c_lab = Label(frame, text="= 0").grid(row=1, column=6)

# кнопка "Решить!"
but = Button(frame, text="Решить!", command=handler).grid(row=1, column=7, padx=(10,0))

# место для вывода значений x1 и x2 и дискриминанта
output = Text(frame, bg="White", font="Arial 15", width=35, height=10)
output.grid(row=2, columnspan=8)

# запуск главного окна
root.mainloop()
