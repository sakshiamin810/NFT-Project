# Generated by Django 4.0.3 on 2022-04-04 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_cat_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(default='abc.jpg', upload_to='app/img'),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(default='abc.jpg', upload_to='app/img'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(default='abc.jpg', upload_to='app/img'),
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(default='abc.jpg', upload_to='app/img'),
        ),
    ]
