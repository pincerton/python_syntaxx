# Программа с графическим пользовательским интерфейсом (GUI)

# *** Генератор паролей ***

# импортирование необходимых модулей
import hashlib as h
from tkinter import Tk, Label, Entry, Button, StringVar

# основная функия 
def pwdGenerator(pwd_str: str):
    # кодирование в байт строку
    byte_str = pwd_str.encode()
    # хеширование
    hash_obj = h.sha256(byte_str)
    # преобразование хещ-объекта в обычную строку
    hex_str = hash_obj.hexdigest()[:10]
    # возврат результата
    # print(hex_str)
    return hex_str

# объект окна
app = Tk()

# объекты для хранения строк
in_pwd = StringVar()
out_pwd = StringVar()

# виджет текстовой метки
lbl = Label(text="Пароль:")
lbl.grid(row=0, column=0)

# виджет поля ввода "сырой" пароль
Entry(textvariable=in_pwd).grid(row=0, column=1)

# виджет кнопки
def btn():
    p = pwdGenerator(in_pwd.get())
    out_pwd.set(p)
Button(text="ПУСК", command=btn).grid(row=1, column=0)

# виджет поля вывода результата
Entry(textvariable=out_pwd).grid(row=1, column=1)

# точка входа программы
app.mainloop()

# тестирование 
# pwdGenerator("qwerty")