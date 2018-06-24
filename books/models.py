# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=500,
                                  db_index=True,
                                  verbose_name=u'имя')
    last_name = models.CharField(max_length=500,
                                 db_index=True,
                                 verbose_name=u'фамилия')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = u'автор'


class Publisher(models.Model):
    name = models.CharField(max_length=500,
                            db_index=True,
                            verbose_name=u'название издательства')
    address = models.CharField(max_length=500,
                               verbose_name=u'адрес издательства')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'издательство'


class NetworkDeviceCategory(models.Model):
    name = models.CharField(max_length=500,
                            db_index=True,
                            verbose_name='категория устройства')
    comment = models.CharField(max_length=500,
                               verbose_name='комментарий')

    def __str__(self):
        return self.name


class NetworkDeviceType(models.Model):
    name = models.CharField(max_length=500,
                            db_index=True,
                            verbose_name='тип устройства')
    category = models.ForeignKey(NetworkDeviceCategory,
                                 verbose_name='категрия устройства',
                                 on_delete=models.CASCADE)
    comment = models.CharField(max_length=500,
                               verbose_name='комментарий')

    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField(max_length=500,
                             db_index=True,
                             verbose_name=u'название книги')
    authors = models.ManyToManyField(Author,
                                     verbose_name=u'авторы')
    publisher = models.ForeignKey(Publisher,
                                  verbose_name=u'издательство',
                                  on_delete=models.CASCADE)
    manually_set_type = models.ForeignKey(NetworkDeviceType,
                                          on_delete=models.CASCADE,
                                          blank=True,
                                          null=True)

    class Meta:
        verbose_name = u'книга'
