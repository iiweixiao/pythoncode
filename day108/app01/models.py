from django.db import models


class UpInfo(models.Model):
    mid = models.CharField(verbose_name='视频主id号', max_length=16)
    name = models.CharField(verbose_name='up主', max_length=32)

    def __str__(self):
        return self.name


class VideoInfo(models.Model):
    name = models.CharField(verbose_name='账号名', max_length=16)
    title = models.CharField(verbose_name='标题', max_length=64)
    href = models.CharField(verbose_name='视频链接', max_length=256)
    created = models.CharField(verbose_name='发布时间', max_length=32)
    status_choice = (
        (0, '未看'),
        (1, '已看'),
    )
    status = models.SmallIntegerField(verbose_name='是否观看', choices=status_choice)
    # check = models.CharField(verbose_name='检查', max_length=16)


class UpVideoList(models.Model):
    # mid = models.CharField(verbose_name='视频主id号', max_length=16)
    title = models.CharField(verbose_name='标题', max_length=64)
    href = models.CharField(verbose_name='视频链接', max_length=256)
    created = models.CharField(verbose_name='发布时间', max_length=32)


class HeJi(models.Model):
    index = models.IntegerField(verbose_name='序号')
    title = models.CharField(verbose_name='标题', max_length=64)
    href = models.CharField(verbose_name='视频链接', max_length=256)
    created = models.CharField(verbose_name='发布时间', max_length=32)


class AjaxForm(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=32)
    sex_choices = (
        (1, '男'),
        (2, '女'),
    )
    sex = models.SmallIntegerField(verbose_name='性别', choices=sex_choices, default=1)
    math = models.IntegerField(verbose_name='数学成绩')
    english = models.IntegerField(verbose_name='英语成绩')
    user = models.ForeignKey(verbose_name='up主', to=UpInfo, on_delete=models.CASCADE)