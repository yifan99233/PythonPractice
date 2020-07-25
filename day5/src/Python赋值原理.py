# a = 123
# print(id(a))


# a = 123
# b = a
# print('123数值的内存地址：', id(123))
# print('修改前a的地址：', id(a))
# print('修改前b的地址：', id(b))
#
# print('=' * 30)
# b = 321
# print('321数值的内存地址：', id(321))
# print('修改后a的地址：', id(a))
# print('修改后b的地址：', id(b))

print('=' * 30)
_list = [1, 2, 3, 4]
print('_list的内容', _list, '_list的地址', id(_list), '_list[0]的地址', id(_list[0]))
_list.append(5)
print('添加元素后，_list的内容', _list, '添加元素后，_list的地址', id(_list), '_list[0]的地址', id(_list[0]))

print('=' * 30)
_list = [1, 2, 3, 4, 5]
print(_list)
print('修改前', '_list[1]的内存地址', id(_list[1]),
      '2的内存地址', id(2), '3的内存地址', id(3), '_list[2]的内存地址', id(_list[2]))

_list[2] = 2
print(_list)
print('修改后', '_list[1]的内存地址', id(_list[1]),
      '2的内存地址', id(2), '3的内存地址', id(3), '_list[2]的内存地址', id(_list[2]))
