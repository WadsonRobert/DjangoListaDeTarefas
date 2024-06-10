# Generated by Django 5.0.6 on 2024-06-03 22:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0004_remove_task_done_delete_completed_delete_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Completed',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('options', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('done', models.ForeignKey(default='2', on_delete=django.db.models.deletion.PROTECT, related_name='task_doneORnot', to='tasks.completed')),
            ],
        ),
    ]
