# Generated by Django 3.0.6 on 2020-06-04 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20200604_0543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phonemodel',
            name='body',
        ),
        migrations.RemoveField(
            model_name='phonemodel',
            name='media_url',
        ),
    ]