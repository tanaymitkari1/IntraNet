# Generated by Django 3.0 on 2020-04-02 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ECA', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_eca',
            name='status',
            field=models.CharField(default='active', max_length=10),
        ),
    ]