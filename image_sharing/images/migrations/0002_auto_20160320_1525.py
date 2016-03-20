# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': '图片', 'verbose_name_plural': '图片'},
        ),
        migrations.AlterField(
            model_name='image',
            name='created',
            field=models.DateField(verbose_name='创建时间', db_index=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.TextField(verbose_name='简介', blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(verbose_name='图片', upload_to='images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='image',
            name='slug',
            field=models.SlugField(max_length=200, verbose_name='连体标题', blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=200, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.URLField(verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='image',
            name='users_like',
            field=models.ManyToManyField(verbose_name='喜欢的用户列表', to=settings.AUTH_USER_MODEL, related_name='images_liked', blank=True),
        ),
    ]
