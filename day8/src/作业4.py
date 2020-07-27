while True:
    try:
        _num = int(input('请输入数字：'))
    except ValueError as e:
        print('对方不想和你说话并抛出了一个异常！', e)
    else:
        print(_num)
        exit(0)
