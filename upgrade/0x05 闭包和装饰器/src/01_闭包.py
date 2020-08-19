# 定义一个外部函数
def external(num1):
    # 定义一个内部函数
    def _inner(num2):
        # 内部函数使用了外部函数的变量(num1)
        print('num1的数值为', num1, 'num2的数值为', num2)
        result = num1 + num2
        print("结果是:", result)

    # 外部函数返回了内部函数，这里返回的内部函数就是闭包
    return _inner


# 创建闭包实例
func = external(1)
# 执行闭包
func(2)
func(3)
