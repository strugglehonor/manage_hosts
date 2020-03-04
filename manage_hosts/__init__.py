from django.db.models.signals import pre_save, post_save
import time

def preSave(sender, **kwargs):
    print('一个model对象准备保存')

def postSave(sender, **kwargs):
    print('一个model对象成功保存')

# 注册函数
post_save.connect(preSave)
pre_save.connect(postSave)

