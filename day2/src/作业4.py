# 定义一个空列表
userInfo = []
while True:
    # 获取用户输入信息
    name = input('请输入姓名：')
    age = int(input('请输入年龄：'))
    phone = input('请输入手机号：')

    # 将用户信息加入列表中
    userInfo.append([name, age, phone])

    # 是否结束输入
    _exit = input('是否结束输入（Y/N）：')
    if _exit == 'Y' or _exit == 'y':
        break

# 打印信息
print(userInfo)