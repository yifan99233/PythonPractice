while True:
    # 获取用户账号密码
    userName = input('请输入用户名：')
    passWord = input('请输入密码：')
    # 判断账号密码是否正确
    if userName == 'python' and passWord == '123456':
        print('欢迎光临')
        break
    else:
        print('密码错误，请重试！')
