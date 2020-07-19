my_list = ["red", "apples", "orange", "pink", "bananas", "blue", "black", "white"]

word_list = []
# 遍历列表
for word in my_list:
    # 判断元素是否以s或e结尾
    if word.endswith('s') or word.endswith('e'):
        # 将元素加入列表中
        word_list.append(word)

print(word_list)
