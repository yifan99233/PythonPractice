# 创建生成器
_generator = (i * 2 for i in range(5))
_generator2 = (i * 2 for i in range(5))
print(_generator)
print(_generator2)

# next获取生成器下一个值
value = next(_generator)
value2 = next(_generator)
print(value)
print(value2)

print('===' * 10)
# 遍历生成器
for value in _generator2:
    print(value)
