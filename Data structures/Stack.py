class Stack:
    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if len(self.values) < 1:
            print("Empty Stack")
        else:
            return self.values.pop()

    def peek(self):
        if len(self.values) < 1:
            print("Empty Stack")
            return None
        else:
            return self.values[-1]

    def is_empty(self):
        if not self.values:
            return True
        else:
            return False

    def size(self):
        return len(self.values)
