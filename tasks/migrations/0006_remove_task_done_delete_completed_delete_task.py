# Generated by Django 5.0.6 on 2024-06-03 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='done',
        ),
        migrations.DeleteModel(
            name='Completed',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
