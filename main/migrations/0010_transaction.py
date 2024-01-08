# Generated by Django 4.2.7 on 2023-12-12 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_client_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('balance', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.client')),
            ],
        ),
    ]