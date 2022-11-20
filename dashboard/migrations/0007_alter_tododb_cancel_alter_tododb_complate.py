# Generated by Django 4.1.1 on 2022-11-20 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_tododb_options_alter_tododb_slave_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tododb',
            name='cancel',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dashboard.cancel_task'),
        ),
        migrations.AlterField(
            model_name='tododb',
            name='complate',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dashboard.complate_task'),
        ),
    ]
