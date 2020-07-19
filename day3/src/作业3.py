product = [
    {"name": "电脑", "price": 7000},
    {"name": "鼠标", "price": 30},
    {"name": "usb电动小风扇", "price": 20},
    {"name": "遮阳伞", "price": 50},
]

# 定义变量保存小明有多少钱，定义变量保存小明购买全部物品需要多少钱
_have = 8000
_need = 0

# 遍历列表，获取物品
for _product in product:
    # 读出物品价格，并进行累加
    _need += _product["price"]

# 判断小明是否能购买全部物品
if _have < _need:
    print("不能")
else:
    print("能")

