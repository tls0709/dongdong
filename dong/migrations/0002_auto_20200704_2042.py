# Generated by Django 3.0.7 on 2020-07-04 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dong', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='person',
            old_name='first_mane',
            new_name='first_name',
        ),
    ]
