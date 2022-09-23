value = []
print('请输入逗号分隔的4位二进制数：')
items = [x for x in input().split(',')]
# print(items)
for p in items:
    intp = int(p, 2)
    # print(intp)
    if not intp % 5:
        value.append(p)

print(','.join(value))
