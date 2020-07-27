# 定义类
class Fox(object):
    def run(self):
        print('跑！')

    def say_hello(self, _name):
        print(_name, '，你好哇')


# 创建对象
_fox = Fox()

# 调用方法
_fox.say_hello('星尘')
