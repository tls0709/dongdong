# Generated by Django 3.0.7 on 2020-07-04 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dong', '0002_auto_20200704_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
