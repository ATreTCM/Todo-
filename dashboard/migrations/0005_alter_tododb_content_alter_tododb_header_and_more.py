# Generated by Django 4.0.4 on 2022-05-14 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_tododb_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tododb',
            name='content',
            field=models.TextField(max_length=500, verbose_name='Задача'),
        ),
        migrations.AlterField(
            model_name='tododb',
            name='header',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='tododb',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='tododb',
            name='slave',
            field=models.CharField(blank=True, max_length=100, verbose_name='Виконавець'),
        ),
    ]
