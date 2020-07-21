def cut_str(_str: str, _cur: int, _num: int) -> str:
    return _str[:_cur] + _str[_cur + _num:]


if __name__ == '__main__':
    s = "123456789"
    a1 = 2
    a2 = 4
    print(cut_str(s, a1, a2))
