# 定义类
class Fox(object):
    def run(self):
        print('跑！')

# 创建对象
_fox = Fox()
# 添加属性
_fox.name = '机智的狐狸菌'
_fox.rbq = ['滕青']
print(_fox.name)
print(_fox.rbq)

# 修改属性
_fox.name = '狐狸菌'
_fox.rbq.append('苏苏')
print(_fox.name)
print(_fox.rbq)