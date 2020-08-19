def check(func):
    def inner(_str):
        print("检查文件中....")
        func(_str)
    return inner

@check
def read_file(_str):
    print("正在读取文件中...")
    print('读取到文件：', _str)

# 使用装饰器来装饰函数
if __name__ == '__main__':
    read_file('苏苏の女装照.jpg')