def check(func):
    def inner(_str):
        print("检查文件中....")
        _result = func(_str)
        return _result
    return inner

@check
def read_file(_str):
    print("正在读取文件中...")
    return '读取到文件：' + _str

# 使用装饰器来装饰函数
if __name__ == '__main__':
    _data = read_file('星尘の女装照.jpg')
    print(_data)