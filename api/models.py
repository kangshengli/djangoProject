from django.db import models


class ClientUserScore(models.Model):
    client_no = models.IntegerField(verbose_name='客户端号')
    score = models.IntegerField(verbose_name='客户端用户分数')

    class Meta:
        db_table = 'client_user_score'
