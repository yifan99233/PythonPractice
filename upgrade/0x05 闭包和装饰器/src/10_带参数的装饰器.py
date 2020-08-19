def check_file(extension):
    def check(fn):
        def inner(_fileName):
            if _fileName.endswith(extension):
                result = fn(_fileName)
            else:
                _fileName = _fileName + extension
                result = fn(_fileName)
            return result

        return inner

    return check


@check_file('.zip')
def road_file(_file):
    print('文件读取中...')
    print('读取到文件：', _file)


road_file('星尘の女装合集')
print('===' * 10)
road_file('莉莉の私房照.zip')
