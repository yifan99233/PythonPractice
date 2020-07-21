def print_square():
    for i in range(0, 5):
        print('* ' * 5)


def print_triangle():
    for i in range(1, 6):
        print('* ' * i)


if __name__ == '__main__':
    while True:
        _case = input('请选择功能（1.打印正方形 2.打印三角形 3.退出程序）：')
        if _case == '1':
            print_square()
        elif _case == '2':
            print_triangle()
        elif _case == '3':
            exit(0)
        else:
            print('错误的输入，请重新输入')
