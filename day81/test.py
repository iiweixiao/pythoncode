import os

path1 = os.path.abspath(__file__)  # 获取当前文件绝对路径
path2 = os.path.dirname(path1)  # path1上级目录

print(path1)
print(path2)


A_DIR = os.path.join('User/abc', 'B')
print(A_DIR)