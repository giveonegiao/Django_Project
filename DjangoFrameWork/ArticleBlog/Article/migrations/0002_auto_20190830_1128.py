# Generated by Django 2.1.8 on 2019-08-30 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='click',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='recommend',
            field=models.IntegerField(default=0),
        ),
    ]
