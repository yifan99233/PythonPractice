if __name__ == '__main__':
    _file = open('myfile.txt', 'w')
    _file.write('人生苦短，我用Python')
    _file.close()

    _file = open('myfile.txt', 'r')
    _line = _file.readline()
    _file.close()
    print(_line)
