import datetime

from django.db import models
class contestant(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=100,null=True,default=None, blank=True)
    toph_handle=models.CharField(max_length=100,null=True,default=None, blank=True)
    cf_handle=models.CharField(max_length=100,null=True,default=None, blank=True)
    cc_handle=models.CharField(max_length=100,null=True,default=None, blank=True)
    atcoder_handle=models.CharField(max_length=100,null=True,default=None, blank=True)
    loj_handle=models.CharField(max_length=100,null=True,default=None, blank=True)
    user_email=models.EmailField(max_length=400,null=True,default=None,blank=True)

class atcoder(models.Model):
    sid=models.ForeignKey(contestant,on_delete=models.CASCADE)
    info=models.CharField(max_length=10000,null=True,default=None, blank=True)
    last_update_time=models.CharField(max_length=200,null=True,default=None, blank=True)
class codeforces(models.Model):
    sid=models.ForeignKey(contestant,on_delete=models.CASCADE)
    info=models.CharField(max_length=10000,null=True,default=None, blank=True)
    last_update_time=models.CharField(max_length=200,null=True,default=None, blank=True)
class toph(models.Model):
    sid=models.ForeignKey(contestant,on_delete=models.CASCADE)
    info=models.CharField(max_length=10000,null=True,default=None, blank=True)
    last_update_time=models.CharField(max_length=200,null=True,default=None, blank=True)
class codechef(models.Model):
    sid=models.ForeignKey(contestant,on_delete=models.CASCADE)
    info=models.CharField(max_length=10000,null=True,default=None, blank=True)
    last_update_time=models.CharField(max_length=200,null=True,default=None, blank=True)
class lightoj(models.Model):
    sid=models.ForeignKey(contestant,on_delete=models.CASCADE)
    info=models.CharField(max_length=10000,null=True,default=None, blank=True)
    last_update_time=models.CharField(max_length=200,null=True,default=None, blank=True)

class teams(models.Model):
    member1=models.ForeignKey(contestant,on_delete=models.CASCADE,related_name='member1')
    member2=models.ForeignKey(contestant,on_delete=models.CASCADE,related_name='member2')
    member3=models.ForeignKey(contestant,on_delete=models.CASCADE,related_name='member3')
    team_name=models.CharField(max_length=100,null=True,default=None, blank=True)

class resent_datas(models.Model):
    sid=models.ForeignKey(contestant,on_delete=models.CASCADE)
    rating=models.CharField(max_length=10,null=True,blank=True)
    solved=models.CharField(max_length=10,null=True,blank=True)
    date=models.CharField(max_length=200,null=True,default=None, blank=True)

