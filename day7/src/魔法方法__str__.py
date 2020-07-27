class Fox(object):
    def __init__(self, _name):
        self.name = _name

    def __str__(self):
        return '我叫' + self.name


# 创建对象
_fox = Fox('机智的狐狸菌')
# 调用方法
print(_fox)
