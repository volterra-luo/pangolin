#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from news.models import Staff,Student,Article


admin.site.register(Staff)
admin.site.register(Article)
#admin.site.register(Student)