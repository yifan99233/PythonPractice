class Animal(object):
    def run(self) -> None:
        print('跑起来')


class Cat(Animal):
    def run(self) -> None:
        super().run()
        print('迈着猫步跑起来')

    def eat(self) -> None:
        print('他在恰东西')


_cat = Cat()
_cat.run()
_cat.eat()
