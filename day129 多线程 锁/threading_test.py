import random
from threading import Thread


# 1. 用函数创建多线程
def func(name='fu'):
    for _ in range(2):
        print(f'我是随机数{random.randint(1, 49)}')
        print(f'我是传参{name}')


t1 = Thread(target=func)
t1.start()
t2 = Thread(target=func, args=('lalal',))
t2.start()


# 2. 用类创建多线程
# 1）必须继承类 2）必须复写run函数

class MyThread(Thread):
    def __init__(self, name='moren'):
        super().__init__()
        self.name = name

    def run(self):
        for _ in range(2):
            print(f'我是随机数{random.randint(50, 100)}')
            print(f'我是传参{self.name}')

t3 = MyThread()
t3.start()
t4 = MyThread('guagua')
t4.start()