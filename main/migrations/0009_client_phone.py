# Generated by Django 4.2.7 on 2023-12-12 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_client_amount_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='phone',
            field=models.CharField(default='0763624639', max_length=45),
            preserve_default=False,
        ),
    ]
