from bili import data_all
import pymysql

# print(data_all())
print('connect')
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='12345678', db='day80')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
print('start')
for up_list in data_all():
    if up_list:
        for item in up_list:
            author = item[0]
            title = item[1]
            href = item[2]
            created = item[3]
            print(author,title,)
            sql = 'insert into bili(author, title, href, created) values (%s, %s, %s, %s)'
            cursor.execute(sql, [author, title, href, created])
            conn.commit()
cursor.close()
conn.close()