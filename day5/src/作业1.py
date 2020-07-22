def check_number(_str: str) -> tuple:
    _space = 0
    _digit = 0
    _alpha = 0
    _other = 0
    for _char in _str:
        if _char.isalpha():
            _alpha += 1
        elif _char.isdigit():
            _digit += 1
        elif _char.isspace():
            _space += 1
        else:
            _other += 1
    return _alpha, _digit, _space, _other


if __name__ == '__main__':
    user_input = input("请输入字符串：")
    is_alpha, is_digit, is_space, _others = check_number(user_input)
    print(f'你输入的字符串中有{is_alpha}个字母，{is_digit}个数字，{is_space}个空格和{_others}个其他字符')
