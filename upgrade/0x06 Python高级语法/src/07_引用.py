# 直接赋值
a = [1, 2, 3]
b = a
print(id(a), a)
print(id(b), b)

a[0] = 5  # 修改的是a
print(id(a), a)
print(id(b), b)
