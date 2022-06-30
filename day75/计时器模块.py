import timeit


def prt(num: int):
    for i in range(num):
        print(i, end=' ')
    print('\n')


print(f'运行了{timeit.timeit(lambda : prt(10000), number=1)}秒')

