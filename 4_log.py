# Операции сравнения

x = -3
y = 3

# операция равенства (равно)
# мы спрашиваем "значение х равно значение у?"
res = x == y

# операция неравенства (не равно)
# мы спрашиваем "значение х НЕ равно значение у?"
res = x != y

# операция "меньше"
# мы спрашиваем "значение х меньше значения у?"
res = x < y 

# операция "больше"
# мы спрашиваем "значение х больше значения у?"
res = x > y

# операция "меньше либо равно"
# мы спрашиваем "значение х меньше либо равно значению у?"
x = 3
res = x <= y 

# операция "больше либо равно"
# мы спрашиваем "значение х больше либо равно значению у?"
res = x >= y 


# логические операции

v_1 = True
v_2 = False

# оператор "НЕ" (NOT, инверция, отрицание)
res = not v_1

# оператор "и" (AND, конъюнкция, логическое умножение)
# возвращает True только тогда, когда оба значения True
res = v_1 and v_2

# оператор или (OR, дизъюнкция, логическое сложение)
# # возвращает False только тогда, когда оба значения False
res = v_1 or v_2


a = 10
b = 0
c = -5

res = (a > b ) or not (b == c)


# *****
# отступы в Pythone очень важны!
# по отступам интерпретатор ориентируется во вложенности кода
# Tab - перемещение вправо на один отступ
# Shift + Tab - перемещение влево на один отступ
# *****


# условные операции

a = -10

# оператор if (если)
# if a == 0:
#     print("hello")

# оператор else (иначе)
# if a > -1:
#     res = "больше минус одного"
# else:
#     res = "меньше либо равно минус одному"

# оператор elif (else if)
a = 0

if a > 0:
    res = "больше нуля"
elif a < 0:
    res = "меньше нуля"
else:
    res = "равно нулю"

# print(res)


char = 'b'

if char == 'a':
    res = "буква a"
elif char == 'b':
    res = "буква b"
elif char == 'c':
    res = "буква c"
else:
    res = "этот символ я не знаю :("

print(res)