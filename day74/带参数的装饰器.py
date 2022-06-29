def func_name(name):
    def inner(func):
        def wrapper(*args, **kwargs):
            print(f'运行{name}函数:')
            func(*args, **kwargs)
            print(f'{name}函数运行结束。')
            print('----------')

        return wrapper

    return inner


@func_name('f1')
def f1():
    print('hahahah')


@func_name('f2')
def f2():
    print('esdf')


f1()
f2()
