# Generated by Django 3.1.3 on 2020-12-16 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blogcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='desc',
            field=models.CharField(max_length=5000),
        ),
    ]