# module.py
__all__ = ['_add', '_data']


def _add(a, b):
    return a + b


def _sub(a, b):
    return a - b


_data = '噔噔咚'

print('导包时，我会被执行！')

if __name__ == '__main__':
    print('导包时，我不会被执行！')
