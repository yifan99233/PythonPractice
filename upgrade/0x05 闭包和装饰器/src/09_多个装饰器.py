def fox_say(func):
    def inner():
        return "狐狸：“" + func() + "”"

    return inner


def fox_tail(func):
    def inner():
        return func() + "，咪咕~"

    return inner


@fox_say
@fox_tail
def content():
    return "人生苦短，我用Python"


result = content()
print(result)
