from django.db import models


class UserInfo(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    # t1 = models.IntegerField(default=2)  # 给新增的字段添加默认数据
    # t2 = models.IntegerField(null=True, blank=True)  # 允许新增的字段为空

