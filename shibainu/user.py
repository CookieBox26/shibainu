class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def message(self):
        print(f'{self.name} will turn {self.age + 1} next year.')
