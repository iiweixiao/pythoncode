"""问题:编写一个程序，接受一系列空格分隔的单词作为输入，并在删除所有重复的单词并按字母数字排序后打印这些单词。
假设向程序提供以下输入:
hello world and practice makes perfect and hello world again
则输出为:
again and hello makes perfect practice world
————————————————
版权声明：本文为CSDN博主「Steven灬」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_40547993/article/details/88928075"""

s = input("请输入一段英文句子：")

l = s.split()
# 去重
l1 = list(set(l))
print(l1)
# 排序
l2 = sorted(l1)
print(l2)
# 列表转字符串
s1 = ' '.join(l2)
print(s1)