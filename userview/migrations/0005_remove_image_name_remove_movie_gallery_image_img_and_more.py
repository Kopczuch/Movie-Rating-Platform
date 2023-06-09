# Generated by Django 4.2.1 on 2023-05-20 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userview', '0004_image_movie_gallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='name',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='gallery',
        ),
        migrations.AddField(
            model_name='image',
            name='img',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='movie',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='userview.movie'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]