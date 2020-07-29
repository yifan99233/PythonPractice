class Animal(object):
    name = '动物大家族'
    __leg = '四条腿'


class Cat(Animal):
    def __init__(self, _name: str) -> None:
        self.name = _name

    def play(self) -> None:
        print(self.name, '在玩耍')

    @staticmethod
    def run() -> None:
        print('动物们跑起来了')

    @classmethod
    def eat(cls) -> None:
        print(cls.name, '在恰饭')


_cat = Cat('波斯猫')
_cat.play()
_cat.run()
_cat.eat()
print(_cat.name)
