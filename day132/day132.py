import time


def eat():
    food = None
    while True:
        if food:
            print("小明吃完{}了".format(food))
        food = yield
        print("小明要开始吃{}...".format(food))
        time.sleep(1)


# food = None
MING = eat()  # 产生一个生成器
MING.send(None)  # 预激
food = "面包"
MING.send('面包')
MING.send('苹果')
MING.send('香肠')
