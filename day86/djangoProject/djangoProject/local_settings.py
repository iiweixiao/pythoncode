LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'ASIA/Shanghai'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_fuxi',
        'USERNAME': 'root',
        'PASSWORD': '12345678',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}