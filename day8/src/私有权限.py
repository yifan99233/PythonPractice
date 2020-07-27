class Fox(object):
    def __init__(self):
        self.__tail_count = 0  # 私有属性，只能在类内访问
        self.age = 24  # 公有属性

    def get_info(self):
        print(self.__tail_count)
        self.__levelup()
        print('升级了！', self.__tail_count)

    def __levelup(self) -> None:  # 私有方法，只能在类内调用
        self.__tail_count += 1


smartfox = Fox()
print(smartfox.age)
smartfox.get_info()
