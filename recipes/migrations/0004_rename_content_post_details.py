# Generated by Django 4.2.11 on 2024-03-06 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_post_updated_on'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='details',
        ),
    ]
