class Star(object):
    def __init__(self, _name: str, _film: str):
        self.name = _name
        self.film = _film

    def playing(self):
        print(self)

    def __str__(self) -> str:
        return f'{self.name}出演了{self.film}，非常好看'


if __name__ == '__main__':
    zhou_xing_chi = Star('周星驰', '功夫')
    zhou_xing_chi.playing()
