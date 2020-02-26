from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=10, verbose_name='username')
    passwd = models.CharField(max_length=20, verbose_name='password')

    class Meta:
        verbose_name = '管理员'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Host(models.Model):
    nid = models.AutoField(primary_key=True)
    ip = models.GenericIPAddressField(db_index=True, protocol='ipv4')
    port = models.IntegerField()
    hostname = models.CharField(max_length=20)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='user')
    b = models.ForeignKey('Business', on_delete=models.CASCADE, related_name='b')

    class Meta:
        verbose_name = '主机信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ip


class Application(models.Model):
    host = models.ManyToManyField('Host')
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = '主机应用'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Business(models.Model):
    b_name = models.CharField(max_length=20)