# Generated by Django 3.1.7 on 2021-06-02 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20210602_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='style',
            name='description',
        ),
        migrations.RemoveField(
            model_name='style',
            name='name',
        ),
    ]
