def _test(_data):
    print('_data In Function = ', id(_data))


a = 10
print('_data Before Function = ', id(a))
_test(a)
print('_data After Function = ', id(a))
