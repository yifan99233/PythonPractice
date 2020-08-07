import threading


def task(count):
    print('复读鸡获得了任务，复读', count, '次')
    for i in range(count):
        print("我是复读鸡！")
    else:
        print("任务执行完成")


if __name__ == '__main__':
    # kwargs: 表示以字典方式传入参数
    sub_thread = threading.Thread(target=task, kwargs={"count": 3})
    sub_thread.start()
