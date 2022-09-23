"""题：编写一个接受句子并计算字母和数字的程序。假设为程序提供了以下输入：
Hello world! 123
然后，输出应该是：
字母10
数字3"""

s = input("输入一个句子（包括字母和数字）：")

num = 0
alpha = 0
number = 0
for i in s:
    if i.isalnum():
        num += 1
    if i.isalpha():
        alpha += 1
    if i.isdigit():
        number += 1

print(f'字母有{alpha}个')
print(f'数字有{number}个')
print(f'字母和数字有{num}个')