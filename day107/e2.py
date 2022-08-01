l1 = map(lambda x: x * 2, [1, 2, 3, 4, 5])
print(type(l1))
for i in l1:
    print(i)

l2 = filter(lambda x: x < 0, [-5, -1, 4, 6, 7])
print(type(l2))
for i in l2:
    print(i)

from functools import reduce

l3 = reduce(lambda x, y: x + y, [1, 3, 5, 7])
print(type(l3))
print(l3)