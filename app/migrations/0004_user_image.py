# Generated by Django 4.0.4 on 2022-04-28 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product_image1_product_image2_product_image3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='abc.jpg', upload_to='img/'),
        ),
    ]
