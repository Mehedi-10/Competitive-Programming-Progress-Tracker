from django.db import models
class contestant(models.Model):
    sid=models.IntegerField(primary_key=True)
    toph_handle=models.CharField(max_length=100,null=True)
    cf_handle=models.CharField(max_length=100,null=True)
    cc_handle=models.CharField(max_length=100,null=True)
    atcoder_handle=models.CharField(max_length=100,null=True)
    loj_handle=models.CharField(max_length=100,null=True)

class atcoder(models.Model):
    sid=models.ForeignKey(contestant,on_delete=models.CASCADE)
    info=models.CharField(max_length=10000,null=True)
    last_update_time=models.TimeField()
class codeforces(models.Model):
    sid=models.ForeignKey(contestant,on_delete=models.CASCADE)
    info=models.CharField(max_length=10000,null=True)
    last_update_time=models.TimeField()
class toph(models.Model):
    sid=models.ForeignKey(contestant,on_delete=models.CASCADE)
    info=models.CharField(max_length=10000,null=True)
    last_update_time=models.TimeField()
class codechef(models.Model):
    sid=models.ForeignKey(contestant,on_delete=models.CASCADE)
    info=models.CharField(max_length=10000,null=True)
    last_update_time=models.TimeField()
class lightoj(models.Model):
    sid=models.ForeignKey(contestant,on_delete=models.CASCADE)
    info=models.CharField(max_length=10000,null=True)
    last_update_time=models.TimeField()
