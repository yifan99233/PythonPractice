# 获取年龄
age = int(input('请输入年龄：'))

if age in range(0, 18):
    print('您的年龄是 %d，青少年' % age)
elif age in range(18, 35):
    print('您的年龄是 %d，青年' % age)
elif age in range(35, 60):
    print('您的年龄是 %d，中年' % age)
elif 60 <= age:
    print('您的年龄是 %d，老年' % age)
else:
    # 错误处理
    print('错误的数值！')