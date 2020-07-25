class Star(object):
    def __init__(self, _name: str, _film: str):
        self.name = _name
        self.film = _film

    def __str__(self) -> str:
        return f'{self.name}是我的偶像，我非常喜欢他的电影{self.film}'


if __name__ == '__main__':
    zhou_xing_chi = Star('周星驰', '功夫')
    print(zhou_xing_chi)
