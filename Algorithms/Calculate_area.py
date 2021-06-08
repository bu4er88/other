class Perimeter:
    def __init__(self, side1, side2):
        self.__side1 = side1
        self.__side2 = side2
        self.__perimeter = None

    @property
    def side1(self):
        return self.__side1

    @side1.setter
    def side1(self, value):
        self.__side1 = value
        self.__perimeter = None

    @property
    def side2(self):
        return self.__side2

    @side2.setter
    def side2(self, value):
        self.__side2 = value
        self.__perimeter = None

    @property
    def perimeter(self):
        if self.__perimeter is None:
            self.__perimeter = (self.__side1 + self.__side2) * 2
            print('New area has been calculated')
        return self.__perimeter
