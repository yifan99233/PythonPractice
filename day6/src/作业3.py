import codecs


def write_data(_name: str, _data: str):
    with codecs.open(_name, 'w', 'utf8') as _file:
        _file.write(_data)
        print('写入', _name, '文件成功！')


def read_data(_name: str) -> str:
    with codecs.open(_name, 'r', 'utf8') as _file:
        _data = _file.read()
        print('读取', _name, '文件成功！')
        return _data


if __name__ == '__main__':
    # 初始化作业题目
    write_data('A', 'python是我用过的最好用，最优雅的计算机语言，没有之一！！！')

    # 开始写作业
    # 读文件
    file_data = read_data('A')
    # 分割字符串
    data_list = file_data.split('，')
    for _index, _str in enumerate(data_list):
        # 嘿嘿嘿，你猜我在干什么
        tmp_filename = chr(ord('A') + _index + 1)
        write_data(tmp_filename, _str)
