# Generated by Django 4.0 on 2022-03-07 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0003_blog_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]