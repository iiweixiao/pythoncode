"""
题：使用生成器定义一个类，该生成器可以在给定范围0和n之间迭代可被7整除的数字。
提示：考虑使用yield。
"""

def num(n):
    for i in range(n+1):
        if i % 7 == 0:
            yield i

for i in num(56):
    print(i)