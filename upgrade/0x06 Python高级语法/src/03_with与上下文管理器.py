class File(object):

    # 初始化方法
    def __init__(self, _name, _op):
        # 定义变量保存文件名和打开模式
        self.fileName = _name
        self.operator = _op

    # 上文方法
    def __enter__(self):
        print("进入上文方法")
        self.file = open(self.fileName,self.operator)
        return self.file

    # 下文方法
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('进入下文方法')
        if exc_type == None:
            print('PASS')
        else:
            print('Type: ', exc_type)
            print('Value:', exc_val)
            print('TreacBack:', exc_tb)
        # 返回值决定了捕获的异常是否继续向外抛出
        # 如果是 False 那么就会继续向外抛出，程序会看到系统提示的异常信息
        # 如果是 True 不会向外抛出，程序看不到系统提示信息，只能看到else中的输出
        return True


if __name__ == '__main__':
    # 使用with管理文件
    with File("fox.txt", "r") as file:
        _data = file.read()
        print(_data)