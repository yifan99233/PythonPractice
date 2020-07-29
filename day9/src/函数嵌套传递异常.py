def func1():
    print('start func1')
    print(a)
    print('end func1')


def func2():
    print('start func2')
    func1()
    print('end func2')


def func3():
    print('start func3')
    try:
        func2()
    except Exception as e:
        print('func3 got the err:', e)
    print('end func3')


func3()
