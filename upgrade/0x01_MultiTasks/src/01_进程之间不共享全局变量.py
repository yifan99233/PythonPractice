import multiprocessing

# 定义全局变量
_list = list()


# 添加数据的任务
def add_data():
    for i in range(5):
        _list.append(i)
    # 代码执行到此，说明数据添加完成
    print("写入子进程读出数据：", _list)


def read_data():
    print("读取子进程读出数据：", _list)


if __name__ == '__main__':
    # 创建添加数据的子进程
    add_data_process = multiprocessing.Process(target=add_data)
    # 创建读取数据的子进程
    read_data_process = multiprocessing.Process(target=read_data)
    # 启动子进程执行对应的任务
    add_data_process.start()
    # 主进程等待添加数据的子进程执行完成以后程序再继续往下执行，读取数据
    add_data_process.join()
    read_data_process.start()
    print("主进程读取数据：", _list)
