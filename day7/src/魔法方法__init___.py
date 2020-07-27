# class Fox(object):
#     def __init__(self):
#         self.name = '机智的狐狸菌'
#         print('Hello World，我被初始化了！')
#
#     def my_info(self):
#         print('我叫', self.name)
#
#
# # 创建对象
# _fox = Fox()
# # 调用方法
# _fox.my_info()


class Fox(object):
    def __init__(self, _name):
        self.name = _name
        print(_name, '被初始化了！')

    def my_info(self):
        print('我叫', self.name)


# 创建对象
_fox = Fox('机智的狐狸菌')
# 调用方法
_fox.my_info()
