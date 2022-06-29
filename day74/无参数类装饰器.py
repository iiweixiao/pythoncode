class Logger(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'{self.func.__name__} is running!')
        return self.func(*args, **kwargs)

@Logger
def func1():
    print('hahahaha')


func1()
