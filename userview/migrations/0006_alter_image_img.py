# Generated by Django 4.2.1 on 2023-05-20 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userview', '0005_remove_image_name_remove_movie_gallery_image_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]