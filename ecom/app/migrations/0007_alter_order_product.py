# Generated by Django 5.0.1 on 2024-02-16 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_order_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
