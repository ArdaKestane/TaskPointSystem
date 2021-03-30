# Generated by Django 3.0.2 on 2020-12-28 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0002_auto_20201128_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='points',
            field=models.IntegerField(default=0, verbose_name='Upvotes'),
        ),
        migrations.AddField(
            model_name='comment',
            name='response_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.Comment'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Task'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='vote_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Creation Accepted'), (2, 'Creation Change Requested'), (3, 'Submission Accepted'), (4, 'Submission Change Requested')], default=1, verbose_name='Vote Type'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='voter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]