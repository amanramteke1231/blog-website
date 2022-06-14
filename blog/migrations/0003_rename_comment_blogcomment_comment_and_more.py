# Generated by Django 4.0.4 on 2022-05-02 09:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogcomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcomment',
            old_name='Comment',
            new_name='comment',
        ),
        migrations.RemoveField(
            model_name='blogcomment',
            name='time',
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
