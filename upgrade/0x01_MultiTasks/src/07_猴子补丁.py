import gevent
import time
from gevent import monkey

monkey.patch_all()  # 打补丁


def sing():
    for _ in range(3):
        print('singing~')
        time.sleep(1)


def dance():
    for _ in range(3):
        print('dancing~')
        gevent.sleep(1)


if __name__ == '__main__':
    g1 = gevent.spawn(sing)
    g2 = gevent.spawn(dance)
    g1.join()
    g2.join()
