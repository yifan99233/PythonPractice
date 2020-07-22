_list = [1, 2, 3]


def _add(a: list):
    print(a, id(a))
    a.append(4)
    print(a, id(a))


print('修改前', _list, id(_list))
_add(_list)
print('修改后', _list, id(_list))
