# Generated by Django 4.1.5 on 2023-01-23 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='url',
        ),
    ]