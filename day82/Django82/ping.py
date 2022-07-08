import os

# 不传递参数
os.system('ping 192.168.31.1')  # cmd 即为Linux 终端命令行指令
# 返回命令执行的状态值
# 输出数字为 0，表示正确执行；
# 输出数字非 0，表示错误执行

# # 传递一个参数
# os.system("shell command argus %s" % argus1)
#
# # 传递两个及以上参数
# os.system("shell command argus %s %s" % (argus1, argus2)