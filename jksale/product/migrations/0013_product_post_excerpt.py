# Generated by Django 3.2.6 on 2021-08-11 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='post_excerpt',
            field=models.TextField(blank=True, null=True),
        ),
    ]
