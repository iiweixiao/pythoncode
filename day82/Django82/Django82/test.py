import pymysql

from bili import data_all



data = data_all()

# 1. 连接数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='12345678', db='day80')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 2. 发送指令
for up_list in data:
    if up_list:
        for item in up_list:
            author = item[0]
            title = item[1]
            href = item[2]
            created = item[3]
            cursor.execute('select * from bili where href = %s', [href, ])
            if not cursor.fetchone():
                sql = 'insert into bili(author, title, href, created) values (%s, %s, %s, %s)'
                cursor.execute(sql, [author, title, href, created])
                conn.commit()

sql1 = 'select * from bili order by author asc'
cursor.execute(sql1)
data_list = cursor.fetchall()
contents = {
    'data_list': data_list
}
print(contents)
# 3. 关闭连接
cursor.close()
conn.close()