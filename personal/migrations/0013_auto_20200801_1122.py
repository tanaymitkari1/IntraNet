# Generated by Django 3.0 on 2020-08-01 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0012_auto_20200801_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='price',
            field=models.FloatField(blank=True, default='user.png', null=True),
        ),
    ]
