"""
Создайте класс Person, у которого есть:
конструктор __init__, принимающий 3 аргумента: name, surname, gender.
Атрибут gender может принимать только 2 значения: "male" и "female", по умолчанию "male".
Если в атрибут gender передается любое другое значение, печатать сообщение:
"Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
переопределить метод __str__ следующим образом:
если объект - мужчина (атрибут gender = "male"), возвращать строку "Гражданин <Фамилия> <Имя>
если объект - женщина (атрибут gender = "female"), возвращать строку "Гражданка <Фамилия> <Имя>
"""
class Person:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.__gender = gender
        if (self.gender != 'male') and (self.gender != 'female'):
            print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
            self.gender = 'male'

    def __str__(self):
        if self.gender == 'male':
            return f'Гражданин {self.surname} {self.name}'
        else:
            return f'Гражданка {self.surname} {self.name}'


p1 = Person('Chuck', 'Norris')
print(p1) # печатает "Гражданин Norris Chuck"
p2 = Person('Mila', 'Kunis', 'female')
print(p2) # печатает "Гражданка Kunis Mila"
