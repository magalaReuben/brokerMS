# Generated by Django 4.2.7 on 2023-12-12 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_titles_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='broker',
            name='number',
            field=models.CharField(default='0705099093', max_length=45),
            preserve_default=False,
        ),
    ]
