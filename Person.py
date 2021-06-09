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
        self.gender = gender

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        if value not in ['male', 'female']:
            print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
            self.__gender = 'male'
        else:
            self.__gender = value


a = Person('Leam', 'Kavaliou', '12345dfdfsdaf')  # "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
print(a.gender)  # male
a.gender = 'female'
print(a.gender)  # female
