# Generated by Django 3.1.3 on 2020-12-06 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_newblog_date1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
