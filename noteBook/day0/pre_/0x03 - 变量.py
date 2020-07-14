# int整数类型：不带引号的阿拉伯数字的整数。作用：可以做数学运算
num1 = 10
print(type(num1))
print(num1 + 20)

# float浮点数类型：带有小数点的，不带引号的阿拉伯数字。作用：可以做数学运算
num2 = 5.3
print(type(num2))
print(num2 * 6.1)

# str字符串类型：只要带了引号的都是字符串。
# 作用  1.原样输出;
#       2.字符串与字符串只能相加，会变成相连;
#       3.不同的数据类型，是不能进行运算的。乘以除外：字符串乘以数字，会输出多个字符串
str1 = "10"
str2 = "20"
print(type(str1))
print(type(str2))
print(str1 * str2)