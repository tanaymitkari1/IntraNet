# Generated by Django 3.0 on 2020-07-31 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0009_credit_reg_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credit_reg',
            name='total',
        ),
        migrations.AlterField(
            model_name='credit_reg',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personal.UserProfile'),
        ),
    ]
