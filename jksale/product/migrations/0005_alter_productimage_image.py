# Generated by Django 3.2.6 on 2021-08-08 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_productimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
    ]
