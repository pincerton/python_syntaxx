# *** Функции ***

# определение функции
def func_1(param_1, p_2=0):
    print(param_1 ** 2)
    print(param_1 ** 3)
    print(param_1 * p_2)

def func_2(p_1, p_2, p_3):
    s = p_1 + p_2 + p_3
    return s

# # вызов функции
# func_1(100)

res = func_2(10, 20, 10)

# res = res(5, 5, 10)

# print(res)


# *** Классы *** 

# создание класса 
class Human:
    # метод конструктор
    def __init__(self, name="Baaska", a=0):
        # атрибуты (поля, свойства)
        self.name = name
        self.age = a

    # метод - внутренная функция обьекта
    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# создание экземпляров (объектов) класса Human
p0 = Human(a=30)
p1 = Human("Byokke", 25)

# замена значения атрибута
# p0.name = "Xaatunka"

# считывание значений атрибутов
# print(p0.name, p0.age)
# print(p1.name, p1.age)

# вызов метода экземпляров
p0.info()
p1.info()


# Обектно ориентированное програмирование 