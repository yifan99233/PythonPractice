class Fox(object):
    def __init__(self, _name):
        self.name = _name

    def __str__(self):
        return '我叫' + self.name

    def __del__(self):
        print('对象的生命周期结束', self.name, '自己回到了垃圾桶中')


# 创建对象
_fox = Fox('机智的狐狸菌')
# 调用方法
print(_fox)
