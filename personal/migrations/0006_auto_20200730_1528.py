# Generated by Django 3.0 on 2020-07-30 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0005_auto_20200730_1523'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sub_ans',
            old_name='sub_name1',
            new_name='sub_name',
        ),
    ]
