# Generated by Django 3.0.6 on 2020-09-18 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20200917_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='value',
            field=models.PositiveIntegerField(null=True, verbose_name='Значення'),
        ),
    ]
