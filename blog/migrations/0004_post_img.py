# Generated by Django 4.0.4 on 2022-05-06 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_comment_blogcomment_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='', upload_to='photos', verbose_name='My Photo'),
            preserve_default=False,
        ),
    ]
