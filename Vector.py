"""
Cоздайте класс Vector, который хранит в себе вектор целых чисел.  У класса Vector есть:

конструктор __init__, принимающий произвольное количество аргументов. Среди всех переданных аргументов необходимо
оставить только целые числа и сохранить их в атрибут values в виде списка;
переопределить метод __str__ так, чтобы экземпляр класса Vector выводился следующим образом:
"Вектор(<value1>, <value2>, <value3>, ...)", если вектор не пустой. При этом значения должны быть упорядочены по возрастанию;
"Пустой вектор", если наш вектор не хранит в себе значения
"""
class Vector:
    def __init__(self, *args):
        self.values = [value for value in args if isinstance(value, int)]
        self.lenght = len(self.values)

    def __str__(self):
        if self.lenght < 1:
            return "Пустой вектор"

        return f"Вектор{tuple(sorted(self.values))}"

v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2) # печатает "Пустой вектор"
