# Generated by Django 2.1.8 on 2019-09-05 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Django_login', '0002_goods'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='goods_status',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
