def timer(func):
    def wrapper(*args, **kw):
        # t = __builtins__.__dict__['__import__']('time').time()
        ti = __import__('time')  # 相当于import time as ti
        start = ti.time()

        func(*args, **kw)
        end = ti.time()

        print(f'运行了{end - start}秒...')

    return wrapper


@timer
def count():
    for _ in range(1000):
        print('haha')


count()
