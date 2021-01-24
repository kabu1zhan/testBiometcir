from django.db import models


class Person(models.Model):
    iin = models.CharField(max_length=12, verbose_name='иин')
    age = models.SmallIntegerField(verbose_name='возраст')
