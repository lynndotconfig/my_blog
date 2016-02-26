# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Article(models.Model):
    TAGS = (('F', 'Feeling'), ('W', 'Working'), ('E', 'Entertainment'))

    title = models.CharField(max_length=100)  # 博客题目
    tag = models.CharField(choices=TAGS, max_length=50, blank=True)
    category = models.CharField(max_length=50, blank=True)  # 博客标签
    date_time = models.DateTimeField(auto_now_add=True)  # 博客日期
    content = models.TextField(blank=True, null=True)  # 博客文字正文

    def get_absolute_url(self):
        path = reverse('detail', kwargs={'pk': self.id})
        return "http://127.0.0.1:8000%s" % path

    # python3使用__unicode__, python2使用__str__
    def _str_(self):
        return self.title

    class Meta:
        ordering = ['-date_time']
