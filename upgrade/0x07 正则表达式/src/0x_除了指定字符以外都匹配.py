import re


def check(data):
    if data:
        print(data.group())
    else:
        print("匹配失败")


# 匹配以数字开头的数据
_data = re.match("[^aeiou]", "hello")
check(_data)
print("===" * 10)
_data = re.match("[^aeiou]", "all")
check(_data)
