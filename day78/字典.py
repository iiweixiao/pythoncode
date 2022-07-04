dict1 = {'a': 'hello', 'b': 'nihao', 'c': 'good'}

# 遍历字典
for a, b in dict1.items():
    print(a, b)

# 更改值
dict1['b'] = 'hi'
print(dict1)

# 更改键，字典内元素顺序会变
dict1['B'] = dict1.pop('b')
print(dict1)

# 通过值，更改键
dict2 = {}
for a, b in dict1.items():
    if b == 'good':
        dict2['C'] = b
    else:
        dict2[a] = b
print(dict2)


# 利用浅拷贝得到字典的副本，通过值，删除元素(不使用copy会报错)
for a, b in dict1.copy().items():
    if b == 'hello':
        del dict1[a]
print(dict1)