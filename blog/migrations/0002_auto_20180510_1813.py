# Generated by Django 2.0.5 on 2018-05-10 18:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='body',
            field=models.TextField(default='defualt'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2018, 5, 10, 18, 13, 11, 548405, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
