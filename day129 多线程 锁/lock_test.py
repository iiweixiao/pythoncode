import threading


def job1():
    global n, lock
    with lock:
        for i in range(100):
            n += 1
            print(f'this is {job1.__name__}, n = {n}')


def job2():
    global n, lock
    with lock:
        for i in range(1000):
            n += 10
            print(f'this is {job2.__name__}, n = {n}')


lock = threading.Lock()
n = 0
j1 = threading.Thread(target=job1)
j1.start()
j2 = threading.Thread(target=job2)
j2.start()
