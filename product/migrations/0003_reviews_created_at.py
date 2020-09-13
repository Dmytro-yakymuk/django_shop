# Generated by Django 3.0.6 on 2020-09-10 13:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата створення'),
            preserve_default=False,
        ),
    ]