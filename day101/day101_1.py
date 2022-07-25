import hashlib


def md5(string):
    salt = 'xxxxxx'
    obj = hashlib.md5(salt.encode('utf-8'))
    obj.update(string.encode('utf-8'))
    return obj.hexdigest()


passwd = md5('123')
print(passwd)
