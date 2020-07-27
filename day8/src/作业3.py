class Human(object):
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    def get_info(self) -> None:
        print(self.__name, ':', self.__age)

    def get_age(self) -> int:
        return self.__age

    def get_name(self) -> str:
        return self.__name

    def mod_name(self, name: str) -> None:
        self.__name = name

    def mod_age(self, age: int) -> bool:
        if 0 <= age <= 100:
            self.__age = age
            return True
        else:
            return False


man1 = Human('张三', 20)
man1.get_info()

man1.mod_age(30)
man1.get_info()

man1.mod_name('李四')
man1.get_info()
