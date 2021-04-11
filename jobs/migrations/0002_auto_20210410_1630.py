# Generated by Django 3.1.7 on 2021-04-10 08:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='job_reponsibility',
            new_name='job_responsibility',
        ),
        migrations.AlterField(
            model_name='job',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_city',
            field=models.SmallIntegerField(choices=[(0, '西安'), (1, '深圳'), (2, '杭州')], verbose_name='工作地点'),
        ),
        migrations.AlterField(
            model_name='job',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='修改时间'),
        ),
    ]
