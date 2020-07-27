class Animal(object):
    def run(self) -> None:
        print('他跑起来了！')


class Cat(Animal):
    def eat(self) -> None:
        print('他在吃东西！')


cat1 = Cat()
cat1.run()
cat1.eat()