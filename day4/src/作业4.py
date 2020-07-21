# 方法一：传统交换法
a = 10
b = 20
print(f'交换前a={a}，b={b}')
_tmp = a
a = b
b = _tmp
print(f'交换后a={a}，b={b}')


# 方法二：
a = 10
b = 20
print(f'交换前a={a}，b={b}')
a, b = b, a
print(f'交换后a={a}，b={b}')
