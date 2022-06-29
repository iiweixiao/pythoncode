def logger(func):
    def wrapper(*args, **kw):
        print('start...')

        func(*args, **kw)

        print('end...')

    return wrapper


@logger
def add(x, y):
    print(x + y)


add(1, 2)
