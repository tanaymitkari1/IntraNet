# Generated by Django 3.0 on 2020-07-30 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('placement', '0004_remove_answer_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
