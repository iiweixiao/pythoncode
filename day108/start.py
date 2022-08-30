import os

# 获取当前路径，返回str
# os.path.abspath('.')
# os.getcwd()


cmd = 'python3 ' + os.path.abspath('.') + '/manage.py runserver'
print(cmd)

# 终端执行str命令
os.system(cmd)
