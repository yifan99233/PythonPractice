def _test():
    return 10, 20, 30


_data = _test()
print(_data, type(_data))
a, b, c = _test()
print(a, b, c)
