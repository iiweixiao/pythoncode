# 1. 使用in
if 'llo' in 'hello':
    print('yes')

# 2. 使用find
print('hello'.find('lo'))  # 输出3：'lo'在'hello'中的序列为3
print('hello'.find('w'))  # 输出-1：找不到该字符串

# 3. 使用index
print('hello'.index('el'))  # 输出1：'el'在'hello'中的序列为1
try:
    print('hello'.index('el2'))
except ValueError:
    print('找不到"el2"')

# 4. 使用count
print('hello'.count('l'))  # 输出2
print('hello'.count('wl'))  # 输出0

# 5. __contains__
print('hello'.__contains__('el'))  # True
print('hello'.__contains__('ele'))  # False

# 6. 借助operater模块
import operator
print(operator.contains('hello', 'he'))  # True
print(operator.contains('hello', 'heh'))  # False

# 7. 使用正则匹配
import re
print(re.findall('lo', 'hello'))  # ['llo']
print(re.findall('lol', 'hello'))  # []