# Generated by Django 3.1.7 on 2021-09-09 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datawork', '0003_auto_20210908_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='qty',
            field=models.IntegerField(),
        ),
    ]
