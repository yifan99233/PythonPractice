def find_all_pos(num_list: list, target: int) -> tuple:
    '''
    寻找列表中目标元素的下标
    :param num_list: 列表数据
    :param target: 目标
    :return: 以元组的形式返回结果
    '''
    pos_list = []
    for _index, _value in enumerate(num_list):
        if _value == target:
            pos_list.append(_index)
    return tuple(pos_list)


if __name__ == '__main__':
    _list = [3, 6, 1, 4, 1, 5, 6, 1, 3, 6, 2]
    _target = 1
    _pos = find_all_pos(_list, _target)
    print(_pos)
