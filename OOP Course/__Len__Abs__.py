"""
Demonstration of working methods __len__ and __abs__
"""
class Person:
    def __init__(self, name, surname, current_balance, purchase=0):
        self.__name = name
        self.__surname = surname
        self.__current_balance = current_balance
        self.__purchase = purchase
        self.__purchases = 0

    @property
    def current_balance(self):
        return f'Current balance: {self.__current_balance} $'

    @property
    def purchases(self):
        return f'Sum of purchases: {self.__purchases}'

    @property
    def purchase(self):
        return self.__purchase

    @purchase.setter
    def purchase(self, value):
        if isinstance(value, (int, float)):
            self.__current_balance -= value
            self.__purchases += value
        else:
            raise TypeError
        return f"You've just made a purchase for the amount {value} $\nThe remaining amount on the balance is {self.__current_balance} $"

    # To get length of full name by calling len(attribute) we should create method __len__
    def __len__(self):
        return len(self.__name + self.__surname)

a = Person('Mike', 'Solisbury', 100)
print(len(a))  # print 13
a.purchase = 10
a.purchase = 20
print(a.purchases)  # print 30 $
print(a.current_balance)  # print 70 $
