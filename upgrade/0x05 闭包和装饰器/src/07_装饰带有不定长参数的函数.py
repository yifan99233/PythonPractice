def check(func):
    def inner(*args, **kwargs):
        print("检查文件中....")
        func(*args, **kwargs)
    return inner

@check
def read_file(*args, **kwargs):
    print("正在读取文件中...")
    _data = ''
    for _info in args:
        _data += str(_info)

    for _info in kwargs.values():
        _data += str(_info)
    print('读取到文件：', _data)

# 使用装饰器来装饰函数
if __name__ == '__main__':
    read_file('星尘の女装照.jpg','苏苏の女装照.jpg')