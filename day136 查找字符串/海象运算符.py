# 1. 重复输入直到符合要求
# while (age := input("Enter my age: ")) != '18':
#     print('try again!')
# print("hahaha, you're right!")


# 2. 读写txt文档,直到结束
# with open('demo.txt', 'r') as f:
#     while f.readline():
#         print(f.readline().strip())

# file = open("demo.txt", "r")
# while True:
#     line = file.readline()
#     if not line:
#         break
#     print(line.strip())
#
# file = open("demo.txt", "r")
# while (line := file.readline()):
#     print(line.strip())


# 3. 推导式
members = [
    {"name": "小五", "age": 23, "height": 1.75, "weight": 72},
    {"name": "小李", "age": 17, "height": 1.72, "weight": 63},
    {"name": "小陈", "age": 20, "height": 1.78, "weight": 82}
]
count = 0


def get_bmi(info):
    global count
    count += 1
    print(f"执行了 {count}次")

    height = info["height"]
    weight = info["weight"]
    return weight / (height ** 2)


# 查出所有会员中过于肥胖的人的 bmi 指数
# fat_bmis = [get_bmi(m) for m in members if get_bmi(m) > 20]
fat_bmis = [bmi for m in members if (bmi := get_bmi(m)) > 20]
print(fat_bmis)
