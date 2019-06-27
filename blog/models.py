from django.db import models


class Post(models.Model):
    text = models.TextField(verbose_name='Текст сообщения', blank=False)
    created_date = models.DateTimeField(verbose_name='Дата сообщения', auto_now=True)
    def __str__(self):
        return str(self.created_date)
    class Meta:
        verbose_name='Cообщения'
        verbose_name_plural='Cообщения'


