def check(func):
    def inner(*args, **kwargs):
        print("检查文件中....")
        _result = func(*args, **kwargs)
        return _result

    return inner


@check
def read_file(*args, **kwargs):
    print("正在读取文件中...")
    _data = ''
    for _info in args:
        _data += str(_info)

    for _info in kwargs.values():
        _data += str(_info)
    return '读取到文件：' + _data


@check
def write_file(_data):
    print('写入文件中...')
    print('文件写入成功：', _data)
    return True


# 使用装饰器来装饰函数
if __name__ == '__main__':
    _data = read_file('星尘の女装照.jpg', '苏苏の女装照.jpg')
    print(_data)
    print('===' * 10)
    w_data = write_file('酷儿の私房照.jpg')
    print(w_data)
