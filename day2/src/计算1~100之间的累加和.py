# 定义条件变量 i ，赋值为1
i = 0

# 定义一个辅助变量，用于保存累计的结果
_sum = 0

# while条件（i<=100）
while i <= 100:
    _sum += i
    i += 1

print('_sum = %d' % _sum)
