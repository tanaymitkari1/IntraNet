# Generated by Django 3.0 on 2020-08-01 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0013_auto_20200801_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='image',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='price',
        ),
    ]
