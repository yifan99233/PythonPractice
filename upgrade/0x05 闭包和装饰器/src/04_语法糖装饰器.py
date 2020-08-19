def check(func):
    def inner():
        print("检查文件中....")
        func()
    return inner

@check
def read_file():
    print("正在读取文件中...")

# 使用装饰器来装饰函数
if __name__ == '__main__':
    read_file()