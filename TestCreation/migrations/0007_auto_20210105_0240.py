# Generated by Django 3.1.4 on 2021-01-04 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestCreation', '0006_auto_20210104_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='answer2',
            field=models.CharField(max_length=200, verbose_name='Вариант 2'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='answer3',
            field=models.CharField(max_length=200, verbose_name='Вариант 3'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='answer4',
            field=models.CharField(max_length=200, verbose_name='Вариант 4'),
        ),
    ]
