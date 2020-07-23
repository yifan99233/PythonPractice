if __name__ == '__main__':
    _data = input('请输入字符串：')
    _data = _data.upper()

    with open('test', 'w') as _file:
        _file.write(_data)
