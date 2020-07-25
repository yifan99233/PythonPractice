def test_num(_data: int):
    print('_data In Function = ', _data, '地址：', id(_data))
    _data = 100
    print('_data modify In Function = ', _data, '地址：', id(_data))


_a = 50
print('传入函数前', _a, '地址：', id(_a))
test_num(_a)
print('传入函数后', _a, '地址：', id(_a))

_list = [1, 2, 3]


def test_list(_data: list):
    print('_data In Function = ', _data, id(_data))
    _data.append(4)
    print('_data modify In Function = ', _data, id(_data))


print('修改前', _list, id(_list))
test_list(_list)
print('修改后', _list, id(_list))
