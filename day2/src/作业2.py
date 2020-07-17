# 获取语、数、英成绩
chinese = int(input('请输入语文成绩：'))
math = int(input('请输入数学成绩：'))
english = int(input('请输入英语成绩：'))

# 判断成绩是否合法
if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
    # 计算平均数
    avg = (chinese + math + english) / 3

    if avg > 90:
        print('成绩优秀')
    elif 60 <= avg <= 90:
        print('成绩良好')
    else:
        print('不及格')
else:
    # 错误处理
    print('错误的输入！成绩超出范围')
