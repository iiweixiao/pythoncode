import pymysql
from django.shortcuts import render, HttpResponse

# from bili import data_all


def index(request):
    return HttpResponse('欢迎')


# def bili(request):
#     def bilibili():  # put application's code here
#         """
#         show databases ;
#         use day80;
#         create table bili(
#             id int not null auto_increment primary key ,
#             author varchar(32) not null ,
#             title varchar(64) not null ,
#             href varchar(128) not null ,
#             created datetime);
#         """
#
#     data = data_all()
#
#     # 1. 连接数据库
#     conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='12345678', db='day80')
#     cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#
#     # 2. 发送指令
#     for up_list in data:
#         if up_list:
#             for item in up_list:
#                 author = item[0]
#                 title = item[1]
#                 href = item[2]
#                 created = item[3]
#                 cursor.execute('select * from bili where href = %s', [href, ])
#                 if not cursor.fetchone():
#                     sql = 'insert into bili(author, title, href, created) values (%s, %s, %s, %s)'
#                     cursor.execute(sql, [author, title, href, created])
#                     conn.commit()
#
#     sql1 = 'select * from bili order by author asc'
#     cursor.execute(sql1)
#     data_list = cursor.fetchall()
#
#     # 3. 关闭连接
#     cursor.close()
#     conn.close()
#
#     return render(request, 'bili.html', {'data_list': data_list})


def add_user(request):
    if request.method == 'GET':
        return render(request, 'add_user.html')

    username = request.POST.get('user')
    password = request.POST.get('pwd')
    mobile = request.POST.get('mobile')
    print('haha',username,password,mobile)
    return HttpResponse('ok')