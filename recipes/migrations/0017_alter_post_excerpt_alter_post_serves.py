# Generated by Django 4.2.11 on 2024-03-18 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0016_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.TextField(default='Default excerpt'),
        ),
        migrations.AlterField(
            model_name='post',
            name='serves',
            field=models.IntegerField(choices=[(0, 'Serves 1'), (1, 'Serves 2'), (2, 'Serves 2 - 4'), (3, 'Serves 4 - 6'), (4, 'Serves 8 - 12')], default=0),
        ),
    ]
