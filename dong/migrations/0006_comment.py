# Generated by Django 3.0.7 on 2020-07-04 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dong', '0005_auto_20200704_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=10)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
