# Generated by Django 4.1.2 on 2022-10-28 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_remove_product_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(null=True),
        ),
    ]
