# Generated by Django 3.0.5 on 2020-05-04 09:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taskmanager', '0007_journal_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assignee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Assignee'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(verbose_name='Due Date'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=300, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.IntegerField(verbose_name='Priority'),
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskmanager.Project', verbose_name='Project'),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateField(verbose_name='Start date'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskmanager.Status', verbose_name='Status'),
        ),
    ]
