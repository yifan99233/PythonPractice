class Student(object):
    def __init__(self, _name: str, _age: int, _phone: str) -> None:
        self.name = _name
        self.age = _age
        self.phone = _phone

    def __str__(self) -> str:
        return f'{self.name}\t\t{self.age}\t\t{self.phone}'

    def to_dict(self) -> dict:
        return {'name': self.name, 'age': self.age, 'phone': self.phone}

    @staticmethod
    def to_data(_data: dict) -> object:
        return Student(_data['name'], _data['age'], _data['phone'])


class StudentMgr(object):
    def __init__(self, _db) -> None:
        self.stu_info = []
        self.db = _db

    @staticmethod
    def show_menu() -> None:
        """
        显示菜单
        :return: None
        """
        print('=' * 30)
        print('= 1. 添加学生')
        print('= 2. 查询所有学生')
        print('= 3. 查询某个学生')
        print('= 4. 修改某个学生')
        print('= 5. 删除某个学生')
        print('= 6. 保存信息')
        print('= 7. 退出系统')
        print('=' * 30)

    def add_stu(self) -> None:
        """
        添加学生
        :return: None
        """
        _name = input('请输入学生姓名：')
        _age = int(input('请输入学生年龄：'))
        _phone = input('请输入学生手机：')

        for _stu in self.stu_info:
            if _name == _stu.name:
                print('[W]:学生已存在！')
                break
        else:
            _info = Student(_name, _age, _phone)
            self.stu_info.append(_info)

    def get_stu(self, _name: str = None) -> None:
        """
        查询学生信息
        :param _name: 学生姓名，留空则为遍历列表
        :return: None
        """
        if _name is not None:
            for i, _stu in enumerate(self.stu_info):
                print('序号\t\t姓名\t\t年龄\t\t手机')
                if _stu.name == _name:
                    print(i + 1, '\t\t', _stu)
                    break
            else:
                print(f'[W]:找不到{_name}的相关信息！')
        else:
            print('序号\t\t姓名\t\t年龄\t\t手机')
            for i, _stu in enumerate(self.stu_info):
                print(i + 1, '\t\t', _stu)

    def edit_stu(self, _name: str) -> None:
        """
        修改学生信息
        :param _name: 需要修改信息的学生姓名
        :return: None
        """
        for _stu in self.stu_info:
            if _stu.name == _name:
                _newName = input('请输入新名字：')
                _newAge = int(input('请输入新年龄：'))
                _newPhone = input('请输入新手机：')
                _stu.name = _newName
                _stu.age = _newAge
                _stu.phone = _newPhone
                print('[I]:修改成功！')
                break
        else:
            print(f'[W]:找不到{_name}的相关信息！')

    def del_stu(self, _name: str) -> None:
        """
        删除学生信息
        :param _name: 需要删除信息的学生姓名
        :return: None
        """
        for i, _stu in enumerate(self.stu_info):
            if _stu.name == _name:
                del self.stu_info[i]
                print('[I]:学生删除成功！')
                break
        else:
            print(f'[W]:找不到{_name}的相关信息！')

    def load_data(self) -> None:
        """
        读取数据
        :return: None
        """
        import os
        if not os.path.exists(self.db):
            print('[E]：学生存档不存在')
            return

        _file = open(self.db, 'r')
        try:
            _data = _file.read()
            _stuInfo = eval(_data)
            for _stuData in _stuInfo:
                _info = Student.to_data(_stuData)
                self.stu_info.append(_info)
        except Exception as e:
            print('[E]:学生信息读取异常！', e)
        finally:
            print(f'[I]:学生信息读取完成！共加载了{len(self.stu_info)}个学生')

    def write_data(self) -> None:
        """
        写入数据
        :return: None
        """
        pre_data = []
        for _info in self.stu_info:
            pre_data.append(_info.to_dict())
        save_data = str(pre_data)
        _file = open(self.db, 'w')
        try:
            _file.write(save_data)
        except Exception as e:
            print('[E]：', e)
        else:
            print('[I]：写入完成')

    def start(self) -> None:
        """
        主逻辑方法
        """
        self.load_data()

        while True:
            self.show_menu()
            _case = input('请输入功能功能：')
            if _case == '1':
                self.add_stu()
            elif _case == '2':
                self.get_stu()
            elif _case == '3':
                name = input('请输入学生姓名：')
                self.get_stu(name)

            elif _case == '4':
                name = input('请输入需要修改信息的学生姓名：')
                self.edit_stu(name)
            elif _case == '5':
                name = input('请输入需要删除信息的学生姓名：')
                self.del_stu(name)
            elif _case == '6':
                self.write_data()
            elif _case == '7':
                exit(0)
            else:
                print('[E]：错误的输入！')


if __name__ == '__main__':
    mgr = StudentMgr('stu_info.txt')
    mgr.start()
