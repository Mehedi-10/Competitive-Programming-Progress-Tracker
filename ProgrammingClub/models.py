from django.db import models
class contestant(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=100,null=True,default=None, blank=True)
    toph_handle=models.CharField(max_length=100,null=True,default=None, blank=True)
    cf_handle=models.CharField(max_length=100,null=True,default=None, blank=True)
    cc_handle=models.CharField(max_length=100,null=True,default=None, blank=True)
    atcoder_handle=models.CharField(max_length=100,null=True,default=None, blank=True)
    loj_handle=models.CharField(max_length=100,null=True,default=None, blank=True)

class atcoder(models.Model):
    sid=models.ForeignKey(contestant,on_delete=models.CASCADE)
    info=models.CharField(max_length=10000,null=True,default=None, blank=True)
    last_update_time=models.DateTimeField()
class codeforces(models.Model):
    sid=models.ForeignKey(contestant,on_delete=models.CASCADE)
    info=models.CharField(max_length=10000,null=True,default=None, blank=True)
    last_update_time=models.DateTimeField()
class toph(models.Model):
    sid=models.ForeignKey(contestant,on_delete=models.CASCADE)
    info=models.CharField(max_length=10000,null=True,default=None, blank=True)
    last_update_time=models.DateTimeField()
class codechef(models.Model):
    sid=models.ForeignKey(contestant,on_delete=models.CASCADE)
    info=models.CharField(max_length=10000,null=True,default=None, blank=True)
    last_update_time=models.DateTimeField()
class lightoj(models.Model):
    sid=models.ForeignKey(contestant,on_delete=models.CASCADE)
    info=models.CharField(max_length=10000,null=True,default=None, blank=True)
    last_update_time=models.DateTimeField()

class teams(models.Model):
    member1=models.ForeignKey(contestant,on_delete=models.CASCADE,related_name='member1')
    member2=models.ForeignKey(contestant,on_delete=models.CASCADE,related_name='member2')
    member3=models.ForeignKey(contestant,on_delete=models.CASCADE,related_name='member3')
    team_name=models.CharField(max_length=100,null=True,default=None, blank=True)

