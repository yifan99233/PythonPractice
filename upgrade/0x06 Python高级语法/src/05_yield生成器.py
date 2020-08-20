def _generater(n):
    for i in range(n):
        print('开始第', i + 1, '次生成...')
        yield i
        print('完成第', i + 1, '次生成...')


if __name__ == '__main__':
    _gener = _generater(3)
    # 从中生成一个值
    _point = next(_gener)
    print(_point)

    print('===' * 10)
    for i in _gener:
        print(i)
