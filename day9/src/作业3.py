while True:
    _filename = input('请输入文件名：')
    try:
        _file = open(_filename, 'r')
    except FileNotFoundError as e:
        print(e)
    else:
        try:
            _data = _file.read()
        except Exception as e:
            print(e)
        else:
            print(_data)
            exit(0)
