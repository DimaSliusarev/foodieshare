# Generated by Django 2.2.28 on 2024-03-20 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodieshare', '0011_auto_20240320_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(default='meal.jpg', upload_to='post_images/'),
        ),
    ]
