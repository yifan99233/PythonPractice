_info = [{'name': 'mike', 'age': 34, 'phone': '1341341341'}]


def _menu():
    """
    打印学生管理系统菜单
    :return:
    """
    print('=' * 30)
    print('1. 添加学生信息')
    print('2. 查询所有学生')
    print('3. 查询学生信息')
    print('4. 修改学生信息')
    print('5. 删除学生信息')
    print('6. 退出系统')
    print('=' * 30)


def add_stu():
    """
    添加学生信息
    :return:
    """
    _name = input('请输入姓名：')
    _age = input('请输入年龄：')
    _phone = input('请输入电话号码：')

    for stu_info in _info:
        if stu_info['name'] == _name:
            print(f'列表中已有学生{_name}的信息！')
            break
    else:
        _info.append({'name': _name, 'age': _age, 'phone': _phone})


def search_stu(stu_name: str):
    """
    查询学生信息
    :param stu_name: 传入学生姓名，打印学生相关信息；当传入'all'时，打印全部学生信息；
    :return:
    """
    if stu_name == 'all' or stu_name == 'ALL':
        # 打印全部学生信息
        print("序号\t姓名\t\t年龄\t\t电话号码")
        for _index, stu_info in enumerate(_info):
            print(f'{_index}\t{stu_info["name"]}\t{stu_info["age"]}\t\t{stu_info["phone"]}')

    elif stu_name != '':
        # 打印指定学生信息
        for _index, stu_info in enumerate(_info):
            if stu_info['name'] == stu_name:
                print("序号\t姓名\t\t年龄\t\t电话号码")
                print(f'{_index}\t{stu_info["name"]}\t{stu_info["age"]}\t\t{stu_info["phone"]}')
                break
        else:
            print('未找到该学生信息')
    else:
        # 异常处理
        print('参数错误！')


def edit_stu(stu_name: str):
    """
    修改指定学生名片信息
    :param stu_name: 传入需要修改信息的学生姓名
    :return:
    """
    for _index, stu_info in enumerate(_info):
        if stu_info['name'] == stu_name:
            print('找到该学生信息！')
            ed_name = input('请输入学生姓名：')
            ed_age = int(input('请输入学生年龄：'))
            ed_phone = input('请输入学生手机：')
            _info[_index] = {'name': ed_name, 'age': ed_age, 'phone': ed_phone}
            print('修改学生信息成功！')
            break
    else:
        print('未找到该学生信息')


def del_stu(stu_name: str):
    """
    删除指定学生名片信息
    :param stu_name: 传入需要删除信息的学生姓名
    :return:
    """
    for _index, stu_info in enumerate(_info):
        if stu_info['name'] == stu_name:
            del _info[_index]
            print('删除学生信息成功！')
            break
    else:
        print('未找到该学生信息')


if __name__ == '__main__':
    while True:
        _menu()

        _case = input("请输入功能数字：")
        if _case == '1':
            # 添加学生信息
            add_stu()
        elif _case == '2':
            # 查询所有学生
            search_stu('all')
        elif _case == '3':
            # 查询学生信息
            _name = input("请输入学生姓名：")
            search_stu(_name)
        elif _case == '4':
            # 修改学生信息
            _name = input("请输入学生姓名：")
            edit_stu(_name)
        elif _case == '5':
            # 删除学生信息
            _name = input("请输入学生姓名：")
            del_stu(_name)
        elif _case == '6':
            # 退出系统
            exit(0)
        else:
            print('错误的输入，请重新输入功能数字！')
