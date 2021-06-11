class Names:
    def __init__(self, name):
        self.name = name

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.name):
            raise StopIteration
        letter = self.name[self.index]
        return letter

a = Names('Jacobs Creek')
b = iter(a)

for i in range(0,15):
    print(next(b))
