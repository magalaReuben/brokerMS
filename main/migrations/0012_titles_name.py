# Generated by Django 4.2.7 on 2023-12-12 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_titles_signature_titles_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='titles',
            name='name',
            field=models.CharField(default='Doc', max_length=45),
            preserve_default=False,
        ),
    ]
