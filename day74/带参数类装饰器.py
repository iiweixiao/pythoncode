class Show_info(object):
    def __init__(self, info='green'):
        self.info = info

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print('start...')
            print(f'[{self.info}]: {func.__name__} is running')
            func(*args, **kwargs)
            print('end...')
        return wrapper




@Show_info('Warning')
def func1():
    print('hahahaha')


@Show_info('Safety')
def func2():
    print('good')


func1()
func2()