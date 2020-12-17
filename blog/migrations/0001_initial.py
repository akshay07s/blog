# Generated by Django 3.1.3 on 2020-12-02 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='blog/blogpost/images')),
            ],
        ),
    ]
