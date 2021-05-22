# Generated by Django 3.1.4 on 2021-05-10 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_added_action_record_and_task_difference_models'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actionrecord',
            old_name='action_datetime',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='date',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='date',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='taskdifference',
            old_name='datetime',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='vote',
            old_name='date',
            new_name='created_on',
        ),
        migrations.AlterField(
            model_name='actionrecord',
            name='action_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Task Create'), (2, 'Task Edit'), (3, 'Task Submit'), (4, 'Task Comment'), (5, 'Task Final Comment'), (6, 'Task Creation Accept'), (7, 'Task Status Change To Working On It'), (8, 'Task Creation Request Change'), (9, 'Task Submission Accept'), (10, 'Task Status Change To Waiting For Review'), (11, 'Task Submission Request Change'), (12, 'Task Reject')], default=0, verbose_name='Vote Type'),
        ),
    ]
