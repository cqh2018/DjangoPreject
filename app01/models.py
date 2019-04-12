from django.db import models

# Create your models here.
class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32,unique=True)
    ctime = models.DateTimeField(auto_now_add=True,null=True)
    uptime = models.DateTimeField(auto_now=True,null=True)
class UserInfo(models.Model):
    #id 列，自增，主键
    #用户名列，字符串类型，指定一个长度
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    gender = models.CharField(max_length=60,null=True)
    user_group = models.ForeignKey('UserGroup',to_field='uid',default=1,on_delete=models.CASCADE)

    user_type_choices = (
        (1,'超级用户'),
        (1,'普通用户'),
        (1,'游客'),
    )
    user_type_id = models.ImageField(choices=user_type_choices,default=1)
