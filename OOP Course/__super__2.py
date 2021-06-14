class Initialization:

    def __init__(self, capacity, food):
        if not isinstance(capacity, int):
            print('Количество людей должно быть целым числом')
        else:
            self.capacity = capacity
        self.food = food


class Vegetarian(Initialization):

    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f'{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}'


class MeatEater(Initialization):

    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f'{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}'


class SweetTooth(Initialization):

    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f'Сладкоежек в Москве {self.capacity}. Их самая любимая еда {self.food}'

    def __eq__(self, other):
        if isinstance(other, int):
            if self.capacity == other:
                return f'Количество сладкоежек из опрошенных людей совпадает с {other}'
            else:
                return f'Количество людей не совпадает'
        if isinstance(other, Initialization):  # (MeatEater, SweetTooth)):
            if self.capacity == other.capacity:
                return f'Количество людей среди двух любителей разных типов еды совпало'
            else:
                return f'Количество людей не совпадает'
        return f'Невозможно сравнить количество сладкоежек с {other}'

    def __lt__(self, other):
        if isinstance(other, int):
            if self.capacity < other:
                return f'Количество сладкоежек меньше, чем {other}'
            else:
                return f'Количество сладкоежек в Москве не меньше, чем {other}'
        if isinstance(other, Initialization):  # (MeatEater, SweetTooth)):
            if self.capacity < other.capacity:
                return f'Сладкоежек меньше, чем людей с другим вкусовым предпочтением'
            else:
                return f'Число сладкоежек не меньше количества людей с другим вкусовым предпочтением'
        return f'Невозможно сравнить количество сладкоежек с {other}'

    def __gt__(self, other):
        if isinstance(other, int):
            if self.capacity > other:
                return f'Количество сладкоежек больше, чем {other}'
            else:
                return f'Количество сладкоежек в Москве не больше, чем {other}'
        if isinstance(other, Initialization):  # (MeatEater, SweetTooth)):
            if self.capacity > other.capacity:
                return f'Сладкоежек больше, чем людей с другим вкусовым предпочтением'
            else:
                return f'Число сладкоежек не меньше количества людей с другим вкусовым предпочтением'
        return f'Невозможно сравнить количество сладкоежек с {other}'

    def __str__(self):
        return f'Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}'


v_first = Vegetarian(10000, ['Орехи', 'овощи', 'фрукты'])
print(v_first)  # 10000 людей предпочитают не есть мясо! Они предпочитают ['Орехи', 'овощи', 'фрукты']
v_second = Vegetarian([23], ['nothing'])  # Количество людей должно быть целым числом

m_first = MeatEater(15000, ['Жареную картошку', 'рыба'])
print(m_first)  # 15000 мясоедов в Москве! Помимо мяса они едят еще и ['Жареную картошку', 'рыба']
s_first = SweetTooth(30000, ['Мороженое', 'Чипсы', 'ШОКОЛАД'])
print(s_first)  # Сладкоежек в Москве 30000. Их самая любимя еда: ['Мороженое', 'Чипсы', 'ШОКОЛАД']
print(s_first > v_first)  # Сладкоежек больше, чем людей с другим вкусовым предпочтением
print(30000 == s_first)  # Количество сладкоежек из опрошенных людей совпадает с 30000
print(s_first == 25000)  # Количество людей не совпадает
print(100000 < s_first)  # Количество сладкоежек в Москве не больше, чем 100000
print(100 < s_first)  # Количество сладкоежек больше, чем 100
