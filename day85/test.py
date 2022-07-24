m = __import__("time")
print("__import__(A)结果:", m)

# m = __import__("conf.c_dir")
# print("__import__(A.B)结果:", m)
#
# m = __import__("conf.c_dir", fromlist=[""])
# print("__import__(A.B, fromlist=['B'])结果:", m)
created = m.time()
print(created)

_s = __import__('smtplib')
_e = __import__('email.utils', fromlist=['formataddr', ])
_ee = __import__('email.mime.text', fromlist=['MIMEText', ])

# 邮件文本
msg = __builtins__.__dict__['__import__']('email').mime.text.MIMEText('hahah', "html", "utf-8")
# 邮件上显示的发件人:wx_python
msg["From"] = __builtins__.__dict__['__import__']('email').utils.formataddr(["bili_up", "iiweixiao@yeah.net"])
# 邮件上显示的主题
msg["Subject"] = 'subject'

# 发送邮件
server = __builtins__.__dict__['__import__']('smtplib').SMTP_SSL("smtp.yeah.net")
server.login("iiweixiao@yeah.net", "IHHLUMDULZIKQPQR")  # "发件人的邮箱", "这里填写授权码"
server.sendmail("iiweixiao@yeah.net", 'weixiaot2021@icloud.com', msg.as_string())  # "发件人邮箱", "接受人邮箱"
server.quit()
print('已发送邮件')
# send_email(r_addr, content)

