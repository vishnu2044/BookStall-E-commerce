# Generated by Django 4.2.2 on 2023-07-31 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_offer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='coupon_stock',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]