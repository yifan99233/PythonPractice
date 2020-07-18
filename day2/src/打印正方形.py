# 定义条件变量 i ，赋值为0
i = 0

# 进入外层循环，循环打印每行
while i < 5:
    j = 0
    # 进入内层循环，循环打印一整行
    while j < 5:
        print('*', end=' ')
        j += 1
    print()
    i += 1
