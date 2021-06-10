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
