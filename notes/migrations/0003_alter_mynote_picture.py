# Generated by Django 3.2.5 on 2021-11-01 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20211101_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mynote',
            name='picture',
            field=models.ImageField(upload_to='media'),
        ),
    ]
