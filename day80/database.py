import pymysql

# 添加while循环可以重复给数据库添加数据
# while True:
#     name = input('输入名字：')
#     if name == 'q':
#         break
#     password = input('输入密码：')
#     mobile = input('输入手机号：')

# 1. 连接数据库
conn = pymysql.connect(host='127.0.0.1', user='root', password='12345678', charset='utf8', db='day80')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 2. 发送指令
# 1) 添加数据
sql = 'insert into admin(username, password, mobile) values (%s, %s, %s)'
cursor.execute(sql, [name, password, mobile])
conn.commit()

# 2) 查询数据
cursor.execute('select * from admin where id > %s', [1, ])
data_list = cursor.fetchall()  # fetchone 获取一条信息，如查询密码
for data_dict in data_list:
    print(data_dict)

# 3) 删除数据
cursor.execute('delete from admin where id = %s', [2, ])
conn.commit()

# 4) 修改数据
cursor.execute('update admin set mobile=%s where username=%s', ["133xxxxxxxx", "wx"])
conn.commit()

# 3. 关闭连接
cursor.close()
conn.close()
