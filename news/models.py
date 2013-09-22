#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class Person(models.Model):
    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1,choices=GENDER,default='M')
    img_url = models.ImageField(upload_to='photos/%Y/%m/%d')
    email_address = models.EmailField(u'邮箱')

class Staff(Person):
    office = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = u'职工'

class Student(Person):
    grade = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = u'学生'

    
class Article(models.Model):
    title = models.CharField(u'标题',max_length=100)
    pub_date = models.DateTimeField(u'发布日期')
    author = models.ForeignKey(Staff,verbose_name=u'编辑者')
    content = models.TextField(u'文章内容')
    
    class Meta:
        verbose_name_plural = u'文章'
        verbose_name = u'文章'

app_name = u'新闻信息'