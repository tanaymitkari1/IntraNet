# Generated by Django 3.0 on 2020-04-12 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ECA', '0004_student_list_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_list',
            name='field',
        ),
    ]
