def get_sum(a: int, b: int):
    _tmp = a + b
    if _tmp > 20:
        print('超过10的加法太难了')
    else:
        print('计算结果为：', _tmp)


if __name__ == '__main__':
    _num1 = int(input('请输入第一个数字：'))
    _num2 = int(input('请输入第二个数字：'))
    get_sum(_num1, _num2)
