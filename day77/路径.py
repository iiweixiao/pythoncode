import os

path1 = os.path.abspath(__file__)
print(path1)

path2 = os.path.dirname(path1)
print(path2)
filename = path2 + '/bilibili.py'
print(filename)

path3 = os.path.dirname(path2)
print(path3)
p = os.path.join(path2, 'bilibili.py')
print(p)