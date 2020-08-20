import copy

# 浅拷贝
a = [1, 2, 3]
b = [11, 22, 33]
c = [111, 222, 333]

list01 = [a, b, c]
print('拷贝前,', id(list01))
list02 = copy.deepcopy(list01)
#查看list01 和 list02
# 查看list01 和 list02
print('拷贝后,', id(list01), list01)
print('拷贝后,', id(list02), list02)

print('===' * 10)
# 修改一下
a[0] = 5
print('拷贝后,', id(list01), list01)
print('拷贝后,', id(list02), list02)