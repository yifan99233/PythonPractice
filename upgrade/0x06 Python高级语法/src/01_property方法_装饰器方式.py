class Person(object):
    def __init__(self):
        self.__age = 0

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age >= 150:
            print('成精了')
        else:
            self.__age = new_age

if __name__ == '__main__':
    p = Person()
    print(p.age)
    p.age = 100
    print(p.age)
    p.age = 150