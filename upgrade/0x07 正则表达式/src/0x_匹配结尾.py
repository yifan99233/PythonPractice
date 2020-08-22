import re


def check(data):
    if data:
        print(data.group())
    else:
        print("匹配失败")


# 匹配以数字开头的数据
_data = re.match(".*\d$", "hello5")
check(_data)
print("===" * 10)
_data = re.match(".*\d$", "hellos")
check(_data)
