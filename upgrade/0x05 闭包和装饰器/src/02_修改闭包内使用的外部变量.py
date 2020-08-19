# 定义一个外部函数
def err_external(num1):
    # 定义一个内部函数
    def _inner(num2):
        # 这里本意想要修改外部num1的值，实际上是在内部函数定义了一个局部变量num1
        num1 = 10
        # 内部函数使用了外部函数的变量(num1)
        result = num1 + num2
        print("结果是:", result)
    print('调用内部函数前，闭包外：num1的数值为', num1)
    _inner(1)
    print('调用内部函数后，闭包外：num1的数值为', num1)
    # 外部函数返回了内部函数，这里返回的内部函数就是闭包
    return _inner

# 创建闭包实例
e_func = err_external(1)
print('==='*10)
# 执行闭包
e_func(2)


# 定义一个外部函数
def r_external(num1):
    # 定义一个内部函数
    def _inner(num2):
        # 使用 nonlocal 修饰变量 num1 告诉解释器此处修改的为外部的变量num1
        nonlocal num1
        num1 = 10
        # 内部函数使用了外部函数的变量(num1)
        result = num1 + num2
        print("结果是:", result)

    print('调用内部函数前，闭包外：num1的数值为', num1)
    _inner(1)
    print('调用内部函数后，闭包外：num1的数值为', num1)

    # 外部函数返回了内部函数，这里返回的内部函数就是闭包
    return _inner

# 创建闭包实例
r_func = r_external(1)
print('==='*10)
# 执行闭包
r_func(2)