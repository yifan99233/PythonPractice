class Star(object):
    def __init__(self, _name: str, _film: str):
        self.name = _name
        self.film = _film

    def __str__(self) -> str:
        return f'明星姓名：{self.name},明星的电影：{self.film}'


if __name__ == '__main__':
    zhou_xing_chi = Star('周星驰', '功夫')
    print(zhou_xing_chi)
