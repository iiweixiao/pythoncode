import threading
import os
import socket
import time


def ping_ip(ip):
    global res
    result = os.popen(f'ping -c 1 -t 1 {ip}').read()

    if 'ttl' in result:
        # print(f'{ip} 在线')
        res.append(f'{ip} 在线')


res = []

# 获取本地ip
hostname = socket.gethostname()
while True:
    try:
        local_ip = socket.gethostbyname(hostname)
        if local_ip:
            break
    except:
        pass

time.sleep(0.2)

# 得到本网段所有ip
ip_list = [local_ip.rsplit('.', maxsplit=1)[0] + '.' + str(i) for i in range(1, 255)]




for ip in ip_list:
    sub_thread = threading.Thread(target=ping_ip, args=(ip,), daemon=True)
    sub_thread.start()

# 按ip地址第四位排序
res.sort(key=lambda x: eval(x.split('.')[3].split(' ')[0]))

for i in res:
    print(i)
