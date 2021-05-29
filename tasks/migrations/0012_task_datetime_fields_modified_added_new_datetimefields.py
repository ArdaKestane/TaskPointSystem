# Generated by Django 3.1.4 on 2021-04-29 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0011_added_action_record_and_task_difference_models'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='task',
            name='date',
        ),
        migrations.RemoveField(
            model_name='task',
            name='valid',
        ),
        migrations.AddField(
            model_name='task',
            name='completed_on',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Completed on'),
        ),
        migrations.AddField(
            model_name='task',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created on'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='creation_approved_on',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Creation approved on'),
        ),
        migrations.AddField(
            model_name='task',
            name='submission_approved_on',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Submission approved on'),
        ),
        migrations.AlterField(
            model_name='actionrecord',
            name='actor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='actionrecord',
            name='object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Task title'),
        ),
        migrations.AlterField(
            model_name='taskdifference',
            name='action_record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.actionrecord'),
        ),
        migrations.AlterField(
            model_name='taskdifference',
            name='assignee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.developer'),
        ),
        migrations.AlterField(
            model_name='taskdifference',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task'),
        ),
        migrations.CreateModel(
            name='PointPool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.PositiveIntegerField(default=0)),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.developer')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.team')),
            ],
        ),
    ]