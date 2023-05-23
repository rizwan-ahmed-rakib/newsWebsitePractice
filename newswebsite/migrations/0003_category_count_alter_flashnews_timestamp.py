# Generated by Django 4.2.1 on 2023-05-18 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newswebsite', '0002_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='flashnews',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]