# 注意： gevent是遇到耗时操作， 自动切换
# 哪些是耗时操作: g1.join() gevent.sleep(1)
import gevent


def sing():
    for i in range(3):
        print("唱歌...")
        gevent.sleep(1)  # 出现耗时操作、挂起


def dance():
    for i in range(3):
        print("跳舞...")
        gevent.sleep(1)  # 出现耗时操作、挂起


if __name__ == '__main__':
    g1 = gevent.spawn(sing)
    g2 = gevent.spawn(dance)

    g1.join()  # 主线程等待g1协程执行完成 （耗时操作）
    g2.join()  # 主线程等待g2协程执行完成 （耗时操作）
