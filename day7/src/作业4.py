class Animal(object):
    def run(self):
        print('跑起来了！')


class Cat(Animal):
    def eat(self):
        print('吃猫粮')


class BosiCat(Cat):
    def __init__(self):
        self.name = '波斯猫'
