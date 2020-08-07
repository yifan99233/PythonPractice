import threading


def task(count):
    print('复读鸡获得了任务，复读', count, '次')
    for i in range(count):
        print("我是复读鸡！")
    else:
        print("任务执行完成")


if __name__ == '__main__':
    # args: 以元组的方式给任务传入参数
    sub_thread = threading.Thread(target=task, args=(5,))
    sub_thread.start()
