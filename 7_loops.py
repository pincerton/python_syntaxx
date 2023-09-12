# *** Циклы ***

# Оператор while

# бесконечный цикл
# while True:
#     print("hello")

# цикл с условием
# val = 0

# while val <= 10:
#     print(f"Значение: {val}")
#     # длинный вариант инкремента
#     # val = val + 1
#     # короткий вариант
#     val += 1

# val = 10

# while val > -5:
#     print(f"Значение: {val}")
#     val -= 1

# прерывание цикла по дополнительному условию

# while True:
#     in_val = input("Enter the name: ")
#     if in_val == "stop":
#         print("Chao!")
#         break
#     print(f"Hello, {in_val}!")

# val = 10

# while val > 0:
#     print(val)
#     val -= 1
#     if val < 5:
#         break

# пропуск части кода тела цикла
# val = 0

# while val < 20:
#     # 1 кусок кода
#     print(val)
#     val += 1
#     if val > 10:
#         continue
#     # 2 кусок кода
#     print("hello")


# Оператор for

# 1. "чтение" значения объекта с последовательностьюпо порядку
# 2. считвнное значение присваивается в собственную переменную
# 3. выполняет код своего тела

lst_0 = [10, 20, 30, 4, 3, 100]

# for value in lst_0:
#     value *= 10
#     print(value)

# for char in "python":
#     print(char)

dict_0 = dict(a=100, b=200, c=300)

# print(dict_0)

# for item in dict_0.items():
#     print(item)

# for k, v in dict_0.items():
#     print(f"Key: {k}, Значение: {v}")

# for k in dict_0.keys():
#     print(f"Key: {k}")

# класс range()

r = range(10)
r = range(-10, 20, 2)

# print(r)
# print(tuple(r))

# for n in range(-5, 5):
#     print(n)

# for n in range(5):
#     print("hello")

# безымянная переменная
for _ in range(5):
    print("hello")

# генератор списка
# генератор словаря