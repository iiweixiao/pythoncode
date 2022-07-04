def is_number():
    n = 3
    while n > 0:
        value = input('请输入数字：')
        n -= 1
        try:
            v1 = eval(value)
            return v1
        except:
            pass
        if n == 0:
            print('让你输个数字这么困难？不玩了！')


is_number()
