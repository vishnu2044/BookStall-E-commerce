# Generated by Django 4.2.2 on 2023-08-10 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_order', '0006_alter_order_discount_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='coupon_discount',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='discount_amount',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
