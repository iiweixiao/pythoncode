# for n in range(-99, 10000000000):
#     # print(n)
#     for a in range(1, 100000):
#         if a ** 2 == n + 100:
#             for b in range(a+1, 100000):
#                 if b ** 2 == n + 268:
#                     print(n)

l = []
for i in range(-168, 169):
    for j in range(-168, 169):
        if i * j == 168:
            n = (i**2+j**2)/4-84
            if n % 1 == 0:
                l.append(int(n))
l2 = sorted(list(set(l)))
for item in l2:
    print(item)
