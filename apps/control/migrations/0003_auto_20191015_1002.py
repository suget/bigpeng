# Generated by Django 2.2.6 on 2019-10-15 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0002_auto_20191015_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controleexel',
            name='auto_flag',
            field=models.SmallIntegerField(choices=[(0, '手动'), (1, '自动')], default=0),
        ),
    ]