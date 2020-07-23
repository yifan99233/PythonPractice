class Dog(object):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def eat(self):
        print('吃')


_dog = Dog('大佬', 24)

_dog.eat()
