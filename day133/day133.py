from functools import partial


def power(x, n):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s


power_2 = partial(power, n=2)
power_3 = partial(power, n=3)

# 4的2次方
print('4的2次方:')
print(power_2(4))

# 4的3次方
print('4的3次方:')
print(power_3(4))