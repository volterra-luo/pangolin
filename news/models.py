#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class Person(models.Model):
    GENDER = (
        ('M', '男'),
        ('F', '女'),
    )
    name = models.CharField(u'姓名',max_length=50)
    birth_date = models.DateField(u'出生日期',blank=True,null=True)
    gender = models.CharField(u'性别',max_length=1,choices=GENDER,default='M')
    img_url = models.ImageField(u'头像',upload_to='news/photos/',blank=True)
    email_address = models.EmailField(u'邮箱',blank=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
         abstract = True

class Staff(Person):
    office = models.CharField(u'办公室',max_length=100)
    
    class Meta:
        verbose_name_plural = u'职工'
        verbose_name = u'职工'
        ordering = ['birth_date','name']

class Student(Person):
    grade = models.CharField(u'年级',max_length=100)
    
    class Meta:
        verbose_name_plural = u'学生'
        verbose_name = u'学生'

from django.utils import timezone 
class Article(models.Model):
    title = models.CharField(u'标题',max_length=100)
    pub_date = models.DateTimeField(u'发布日期',blank=True,default=timezone.now())
    author = models.ForeignKey(Staff,verbose_name=u'编辑者')
    content = models.TextField(u'文章内容')
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = u'发布新闻'
        verbose_name = u'发布新闻'

app_lables = u'新闻信息'