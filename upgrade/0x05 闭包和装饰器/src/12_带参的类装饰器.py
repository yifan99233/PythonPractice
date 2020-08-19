class Check_file(object):
    def __init__(self, extension):
        # 初始化操作在此完成
        self.__extension = extension

    # 实现__call__方法，表示对象是一个可调用对象，可以像调用函数一样进行调用。
    def __call__(self, fn):
        # 添加装饰功能
        def check(_fileName):
            if _fileName.endswith(self.__extension):
                result = fn(_fileName)
            else:
                _fileName = _fileName + self.__extension
                result = fn(_fileName)
            return result

        return check


@Check_file('.zip')
def road_file(_file):
    print('文件读取中...')
    print('读取到文件：', _file)


road_file('星尘の女装合集')
print('===' * 10)
road_file('莉莉の私房照.zip')
