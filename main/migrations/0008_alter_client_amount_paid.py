# Generated by Django 4.2.7 on 2023-12-12 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_client_amount_paid_by_remove_client_balance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='Amount_paid',
            field=models.IntegerField(),
        ),
    ]