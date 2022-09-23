import random

print('请选择城市')
print('1.南京 2.无锡 3.徐州 4.常州 5.苏州 6.南通')
s = int(input('请输入城市对应的数字编号：'))
cities = ['南京', '无锡', '徐州', '常州', '苏州', '南通']
city = cities[s - 1]

dict = {'南京': 'A', '无锡': 'B', '徐州': 'C', '常州': 'D', '苏州': 'E', '南通': 'F'}


def r():
    # 没有字母I和字母O
    s = '0123456789ABCDEFGHJKLMNPQRSTUVWXYZ'
    random_card = []
    for _ in range(5):
        n = int(random.random() * len(s))
        random_card.append(s[n])
    return '苏' + dict[city] + '·' + ''.join(random_card)


print(f'你选择的城市是：{city}')
print('随机生成的50个车牌号码如下：')
print('---------------')
# print(r())
for i in range(10):
    for j in range(5):
        print(r(), end='  ')
    print()
