# Generated by Django 3.1.2 on 2020-11-05 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='image_url',
            field=models.URLField(null=True),
        ),
    ]
