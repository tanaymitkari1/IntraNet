# Generated by Django 3.0 on 2020-04-29 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('placement', '0003_auto_20200429_0042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='name',
        ),
    ]
