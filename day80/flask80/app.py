from flask import Flask, render_template, request, redirect

import pymysql

from bili import data_all

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def add_user():  # put application's code here
    if request.method == 'GET':
        return render_template('add_user.html')

    name = request.form.get('user')
    password = request.form.get('password')
    mobile = request.form.get('mobile')
    print(name, password, mobile)

    # 1. 连接数据库
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='12345678', db='day80')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 2. 发送指令
    sql = 'insert into admin(username, password, mobile) values (%s, %s, %s)'
    cursor.execute(sql, [name, password, mobile])
    conn.commit()

    # 3. 关闭连接
    cursor.close()
    conn.close()

    return redirect('/user/info')


@app.route('/user/info', methods=['GET', 'POST'])
def user_info():  # put application's code here

    name = request.form.get('user')
    password = request.form.get('password')
    mobile = request.form.get('mobile')
    print(name, password, mobile)

    # 1. 连接数据库
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='12345678', db='day80')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 2. 发送指令
    sql = 'select * from admin'
    cursor.execute(sql)
    data_list = cursor.fetchall()

    # 3. 关闭连接
    cursor.close()
    conn.close()

    return render_template('user_info.html', data=data_list)


@app.route('/bili', methods=['GET', 'POST'])
def bilibili():  # put application's code here
    """
    show databases ;
    use day80;
    create table bili(
        id int not null auto_increment primary key ,
        author varchar(32) not null ,
        title varchar(64) not null ,
        href varchar(128) not null ,
        created datetime);
    """

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

    # 3. 关闭连接
    cursor.close()
    conn.close()

    return render_template('bili.html', data=data_list)


if __name__ == '__main__':
    app.run()
