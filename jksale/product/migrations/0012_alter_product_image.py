# Generated by Django 3.2.6 on 2021-08-11 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='/user.png', null=True, upload_to='product/'),
        ),
    ]
