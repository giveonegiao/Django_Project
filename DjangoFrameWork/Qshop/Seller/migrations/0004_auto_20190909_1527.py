# Generated by Django 2.1.8 on 2019-09-09 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0003_auto_20190909_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='static/images/default.jpg', upload_to='seller/images'),
        ),
    ]
