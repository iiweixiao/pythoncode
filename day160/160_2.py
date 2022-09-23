"""
机器人从原点（0,0）开始在平面中移动。 机器人可以通过给定的步骤向上，向下，向左和向右移动。 机器人运动的痕迹如下所示：
UP 5
DOWN 3
LETF 3
RIGHT 2
方向之后的数字是步骤。 请编写一个程序来计算一系列运动和原点之后距当前位置的距离。如果距离是浮点数，则只打印最接近的整数。
例：如果给出以下元组作为程序的输入：
UP 5
DOWN 3
LETF 3
RIGHT 2
然后，程序的输出应该是：2
"""
import math

print('请设定移动步骤：')
up = 0
down = 0
left = 0
right = 0
while True:
    s = input().split(' ')
    if s == ['']:
        break
    else:
        if s[0].upper() == 'UP':
            up += int(s[1])
        elif s[0].upper() == 'DOWN':
            down += int(s[1])
        elif s[0].upper() == 'LEFT':
            left += int(s[1])
        elif s[0].upper() == 'RIGHT':
            right += int(s[1])

f = math.sqrt((abs(up - down)) ** 2 + (abs(left - right)) ** 2)
print(int(round(f)))