# Generated by Django 4.1.1 on 2022-11-24 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_alter_tododb_cancel_alter_tododb_complate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complate_task',
            name='users_complate',
        ),
        migrations.AlterField(
            model_name='tododb',
            name='cancel',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tododb',
            name='complate',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Cancel_task',
        ),
        migrations.DeleteModel(
            name='Complate_task',
        ),
    ]
