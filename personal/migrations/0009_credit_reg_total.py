# Generated by Django 3.0 on 2020-07-31 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0008_auto_20200731_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit_reg',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
    ]