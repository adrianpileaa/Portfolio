# Generated by Django 4.0 on 2021-12-27 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_post_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
