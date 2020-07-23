if __name__ == '__main__':
    _filename = input('请输入文件名：')
    _file = open(_filename, 'w')

    _data = input('请输入字符串：')
    for _char in _data:
        if _char == "#":
            break
        else:
            _file.write(_char)
    _file.close()
