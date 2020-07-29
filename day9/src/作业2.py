class AgeError(Exception):
    def __init__(self, _min: int, _max: int, _input: int) -> None:
        super(AgeError, self).__init__()
        self.min = _min
        self.max = _max
        self.input = _input

    def __str__(self) -> str:
        return f'要求年龄介于{self.min}到{self.max}之间，您输入的是{self.input}'


while True:
    try:
        _age = int(input('请输入年龄：'))
    except ValueError as e:
        print('对方不想和你说话并抛出了一个异常:', e)
    else:
        try:
            if 0 <= _age <= 110:
                print('年龄输入正确！')
            else:
                raise AgeError(0, 110, _age)
        except AgeError as e:
            print('年龄输入错误！', e)
        else:
            exit(0)
