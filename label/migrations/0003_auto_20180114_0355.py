# Generated by Django 2.0 on 2018-01-14 03:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('label', '0002_auto_20180112_0807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='label',
            name='parent_id',
        ),
        migrations.AddField(
            model_name='label',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='label',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='label',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='label.Label', verbose_name='父标签ID'),
        ),
    ]